#!/bin/bash
# Merge all video segments into final output - v5 with logo and simplified prompts

OUTPUT_DIR="output"
mkdir -p "$OUTPUT_DIR"

# Video paths from v5 session with logo and updated prompts
GS_PATHS=(
"gs://indigo-night-483404-q4-video-assets/mcp-tool/13510667144128114806/sample_0.mp4"
"gs://indigo-night-483404-q4-video-assets/mcp-tool/1441929405911375081/sample_0.mp4"
"gs://indigo-night-483404-q4-video-assets/mcp-tool/3624632735649951127/sample_0.mp4"
"gs://indigo-night-483404-q4-video-assets/mcp-tool/16958308957766301488/sample_0.mp4"
"gs://indigo-night-483404-q4-video-assets/mcp-tool/6936773382082256879/sample_0.mp4"
"gs://indigo-night-483404-q4-video-assets/mcp-tool/8135177444386040301/sample_0.mp4"
"gs://indigo-night-483404-q4-video-assets/mcp-tool/2445778051170980322/sample_0.mp4"
)

echo "Downloading 7 video segments from GCS..."

# Download each segment using gsutil
for i in "${!GS_PATHS[@]}"; do
    SEG_NUM=$(printf "%02d" $((i+1)))
    echo "Downloading segment $SEG_NUM..."
    gsutil cp "${GS_PATHS[$i]}" "$OUTPUT_DIR/segment_${SEG_NUM}.mp4"
done

echo ""
echo "Creating file list for ffmpeg..."

# Create file list for ffmpeg
cat > "$OUTPUT_DIR/filelist.txt" << 'EOF'
file 'segment_01.mp4'
file 'segment_02.mp4'
file 'segment_03.mp4'
file 'segment_04.mp4'
file 'segment_05.mp4'
file 'segment_06.mp4'
file 'segment_07.mp4'
EOF

echo "Merging videos with ffmpeg..."

# Merge all segments (re-encode for consistency)
cd "$OUTPUT_DIR"
ffmpeg -y -f concat -safe 0 -i filelist.txt -c:v libx264 -c:a aac -movflags +faststart nova_sat_tutorial_v5.mp4

echo ""
echo "============================================"
echo "Done! Final video saved to:"
echo "  output/nova_sat_tutorial_v5.mp4"
echo "============================================"
