#!/usr/bin/env python3
"""Create composite images combining Nova character with Desmos screenshots."""

from PIL import Image
import os

ASSETS_DIR = "assets"
DESMOS_DIR = "assets/desmos"
OUTPUT_DIR = "assets"

# Mapping: (nova_image, desmos_image, output_name)
COMPOSITES = [
    ("nova_waving.png", "desmos_01_empty.png", "view1.png"),           # Intro - waving + empty
    ("nova_pointing.png", "desmos_03_both_equations.png", "view2.png"), # Teaching - pointing + both equations
    ("nova_thinking.png", "desmos_04_zoomed_intersections.png", "view3.png"),  # Thinking + intersections
    ("nova_excited_celebrating.png", "desmos_06_final_answer.png", "view4.png"),  # Celebration + answer
]

def create_composite(nova_path: str, desmos_path: str, output_path: str):
    """Create a composite image with Nova on the left and Desmos on the right."""

    # Load images
    desmos = Image.open(desmos_path).convert("RGBA")
    nova = Image.open(nova_path).convert("RGBA")

    # Target size (1080p aspect ratio)
    target_width = 1920
    target_height = 1080

    # Create white background
    composite = Image.new("RGBA", (target_width, target_height), (255, 255, 255, 255))

    # Resize Desmos to fit right 65% of frame
    desmos_target_width = int(target_width * 0.65)
    desmos_ratio = desmos_target_width / desmos.width
    desmos_new_height = int(desmos.height * desmos_ratio)

    if desmos_new_height > target_height:
        desmos_ratio = target_height / desmos.height
        desmos_new_height = target_height
        desmos_target_width = int(desmos.width * desmos_ratio)

    desmos_resized = desmos.resize((desmos_target_width, desmos_new_height), Image.Resampling.LANCZOS)

    # Position Desmos on the right side
    desmos_x = target_width - desmos_target_width
    desmos_y = (target_height - desmos_new_height) // 2
    composite.paste(desmos_resized, (desmos_x, desmos_y), desmos_resized)

    # Resize Nova to fit left 35% of frame (with some padding)
    nova_target_width = int(target_width * 0.32)
    nova_ratio = nova_target_width / nova.width
    nova_new_height = int(nova.height * nova_ratio)

    # Limit height to 90% of frame
    max_nova_height = int(target_height * 0.9)
    if nova_new_height > max_nova_height:
        nova_ratio = max_nova_height / nova.height
        nova_new_height = max_nova_height
        nova_target_width = int(nova.width * nova_ratio)

    nova_resized = nova.resize((nova_target_width, nova_new_height), Image.Resampling.LANCZOS)

    # Position Nova on the left side, vertically centered (slightly lower)
    nova_x = int(target_width * 0.02)  # 2% padding from left
    nova_y = target_height - nova_new_height - int(target_height * 0.05)  # Bottom aligned with 5% padding

    composite.paste(nova_resized, (nova_x, nova_y), nova_resized)

    # Convert to RGB and save as JPEG
    composite_rgb = composite.convert("RGB")
    composite_rgb.save(output_path, "JPEG", quality=95)
    print(f"Created: {output_path}")

def main():
    for nova_file, desmos_file, output_file in COMPOSITES:
        nova_path = os.path.join(ASSETS_DIR, nova_file)
        desmos_path = os.path.join(DESMOS_DIR, desmos_file)
        output_path = os.path.join(OUTPUT_DIR, output_file)

        if not os.path.exists(nova_path):
            print(f"Warning: Nova image not found: {nova_path}")
            continue
        if not os.path.exists(desmos_path):
            print(f"Warning: Desmos image not found: {desmos_path}")
            continue

        create_composite(nova_path, desmos_path, output_path)

    print("\nDone! Created composite images:")
    for _, _, output_file in COMPOSITES:
        print(f"  - {output_file}")

if __name__ == "__main__":
    main()
