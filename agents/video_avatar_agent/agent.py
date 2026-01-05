# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import google.auth
from google.genai import types

from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_response import LlmResponse
from google.adk.models.llm_request import LlmRequest
from google.adk.tools import AgentTool

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id) # type: ignore
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

from subagents import script_sequencer_agent, video_agent
from utils.storage_utils import upload_data_to_gcs


async def before_model_callback(
    callback_context: CallbackContext,
    llm_request: LlmRequest
) -> LlmResponse | None:
    """The callback that ensures uploading user's images to GCS."""
    persona_views_urls = callback_context.state.get("persona_views", [])
    remove_indexes = []

    upload_persona_views = len(persona_views_urls) == 0

    user_content = llm_request.contents[0]
    for index, part in enumerate(user_content.parts): # type: ignore
        inline_data = part.inline_data
        if (
            not inline_data
            or not inline_data.data
            or not inline_data.mime_type
        ):
            continue
        if inline_data.mime_type.startswith("image/"):
            if upload_persona_views:
                image_url = await upload_data_to_gcs(
                    callback_context.agent_name,
                    inline_data.data,
                    inline_data.mime_type
                )
                persona_views_urls.append(image_url)
            remove_indexes.append(index)
    remove_indexes.reverse()
    for index in remove_indexes:
        user_content.parts.pop(index) # type: ignore
    user_content.parts.append( # type: ignore
        types.Part.from_text(
            text="## VIEW IMAGE URLS\n" + "\n - ".join(persona_views_urls)
        )
    )
    if upload_persona_views:
        callback_context.state["persona_views"] = persona_views_urls


root_agent = LlmAgent(
    name="root_agent",
    model="gemini-2.5-pro",
    instruction="""
    You are a video generation agent for avatar-based training videos. You orchestrate the creation of videos.
    Your input is a character description, a script, and a set of views of the character.

    **Steps**:

    1. Start with `script_sequencer_agent`. It will split the script into smaller chunks and assign a view number to each chunk.
    2. For each script chunk, use `video_agent` to create a video segment.
    3. Present intermediate and final results to the user. The final result must be a numbered list of all videos in the order of the respective script chunks.
    4. After ALL video segments are generated, provide a MERGE SCRIPT that the user can run to combine all videos into one.

    **Rules:**

    -   Make sure to pass the entire Character Description and Video Shot Instructions to `video_agent` tool.
    -   Pass view image URL and view number to `video_agent` tool.
    -   You must present each generated video segment to the user, right after it is generated. Include the video url, the respective chunk number and the script chunk text in the message,
    -   When output "gs://" URIs to the user, replace "gs://" with "https://storage.mtls.cloud.google.com/".
        When calling any functions/tools, keep "gs://" URIs as they are.

    **Final Merge Script:**
    After presenting all video URLs, provide a bash script that:
    1. Downloads all segments from GCS using gsutil
    2. Creates a filelist.txt for ffmpeg
    3. Merges them into a final video using ffmpeg

    Example merge script format (replace URLs with actual generated URLs):
    ```bash
    #!/bin/bash
    mkdir -p output
    # Download segments
    gsutil cp "gs://bucket/path/segment1.mp4" output/segment_01.mp4
    gsutil cp "gs://bucket/path/segment2.mp4" output/segment_02.mp4
    # ... repeat for all segments ...

    # Create filelist
    cd output
    echo "file 'segment_01.mp4'" > filelist.txt
    echo "file 'segment_02.mp4'" >> filelist.txt
    # ... repeat for all segments ...

    # Merge with ffmpeg
    ffmpeg -y -f concat -safe 0 -i filelist.txt -c:v libx264 -c:a aac -movflags +faststart final_video.mp4
    echo "Done! Final video: output/final_video.mp4"
    ```
    """.strip(),
    tools=[AgentTool(script_sequencer_agent), AgentTool(video_agent)],
    before_model_callback=before_model_callback,
)
