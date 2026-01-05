# Learner Labs - AI-Generated SAT Tutorial Videos

This project creates animated SAT math tutorial videos featuring **Nova**, an AI-generated geometric fox character who teaches students how to use Desmos to solve problems quickly and avoid mistakes.

## What We're Building

**Goal:** Generate educational videos where Nova (a purple geometric fox) teaches SAT math concepts using Desmos graphing calculator demonstrations.

**The Challenge:** Using Google's Veo 3.1 model to animate only the character while keeping the background (Desmos graphs, question screens) completely static and unmodified.

## Example Use Case

Nova walks students through solving a system of equations:
- Shows the SAT question
- Opens Desmos and graphs `y = 4x`
- Adds the quadratic `y = x² - 12`
- Finds the intersection point
- Explains the answer with a CTA to practice

**Key Message:** Desmos helps avoid calculation mistakes and solve questions super fast. With practice, students can solve even tough problems in under 30 seconds.

## Architecture

Built on [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/) with:
- **Veo 3.1** for image-to-video generation
- **Gemini 2.5 Flash Image** for image generation
- **MCP Server** for media generation tools

### Agents
- **Orchestrator** - Main agent coordinating video generation
- **Script Sequencer** - Converts content to natural-sounding 8-second script chunks
- **Video Agent** - Generates videos with character animation

## Project Structure

```
assets/
├── prompt.md              # Character description + 7-scene script
├── nova_*.png             # Nova character poses (pointing, thinking, waving, celebrating)
├── desmos/                # Desmos screenshot sequence
├── view1.png - view7.png  # Composite frames (Nova + Desmos/questions)
└── learner-labs-logo.png  # Branding

agents/video_avatar_agent/
├── agent.py               # Main agent definition
└── prompts/video_agent.md # Video generation prompt template

create_views_v2.py         # Script to composite Nova + backgrounds
merge_videos.sh            # Merge video segments with ffmpeg
```

## Video Generation Prompt Strategy

To prevent Veo from adding unwanted artifacts/text overlays:

```
4K high quality video. NO CAMERA MOVEMENT.

Animate ONLY the purple cartoon fox character on the left side:
- Mouth animation in perfect sync with speech
- Modest facial expressions
- Subtle head movements

The fox says: "[SCRIPT]"

Background stays completely frozen and static. Nothing else moves or changes.
```

## Prerequisites

- [Google Cloud Project](https://console.cloud.google.com/) with Vertex AI enabled
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- Python 3.11+
- Access to Veo 3.1 model

## Quick Start

1. Clone and install:
```bash
git clone https://github.com/rgucsb/video-avatars-agent
cd video-avatars-agent
uv venv .venv && source .venv/bin/activate
uv pip install -r agents/video_avatar_agent/requirements.txt
uv pip install -r mcp/requirements.txt
```

2. Configure `.env` with your GCP project ID and bucket name

3. Generate composite view images:
```bash
python create_views_v2.py
```

4. Run the agent:
```bash
adk web agents --port 8082
```

5. Upload view images and submit prompt from `assets/prompt.md`

6. Merge generated segments:
```bash
./merge_videos.sh
```

## Current Status

**Working:**
- Character compositing with Desmos screenshots
- Logo/branding integration
- 7-scene script generation
- Video segment merging

**In Progress:**
- Reducing Veo artifacts on static backgrounds
- Improving prompt engineering for cleaner output

## Credits

Based on [vladkol/video-avatars-agent](https://github.com/vladkol/video-avatars-agent) - AI Agent for Long-form Educational Videos using Google ADK.

## License

Apache 2.0 License - see [LICENSE](LICENSE) file.
