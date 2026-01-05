#!/usr/bin/env python3
"""Create composite view images with correct pointing direction."""

from PIL import Image, ImageOps, ImageDraw, ImageFont
import os
import shutil

ASSETS_DIR = "/Users/rahulgupta2/video-avatars-agent/assets"
DESMOS_DIR = f"{ASSETS_DIR}/desmos"
LOGO_PATH = f"{ASSETS_DIR}/learner-labs-logo.png"

def add_logo(canvas, logo_size=80, margin=20):
    """Add LearnerLabs logo and text to top-left corner of canvas."""
    logo = Image.open(LOGO_PATH).convert("RGBA")
    # Resize logo while maintaining aspect ratio
    logo_ratio = logo.width / logo.height
    logo_height = logo_size
    logo_width = int(logo_height * logo_ratio)
    logo = logo.resize((logo_width, logo_height), Image.LANCZOS)
    # Position in top-left corner
    canvas.paste(logo, (margin, margin), logo)

    # Add text next to logo (two lines)
    draw = ImageDraw.Draw(canvas)
    line1 = "Learner Labs"
    line2 = "Smart SAT Prep"

    # Try to use a nice font, fall back to default
    try:
        font_bold = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 26)
        font_regular = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
    except:
        try:
            font_bold = ImageFont.truetype("/System/Library/Fonts/SFNSText.ttf", 26)
            font_regular = ImageFont.truetype("/System/Library/Fonts/SFNSText.ttf", 20)
        except:
            font_bold = ImageFont.load_default()
            font_regular = ImageFont.load_default()

    # Position text to the right of logo
    text_x = margin + logo_width + 15
    line1_y = margin + 18
    line2_y = margin + 48

    # Draw text in dark color
    draw.text((text_x, line1_y), line1, fill=(33, 33, 33), font=font_bold)
    draw.text((text_x, line2_y), line2, fill=(80, 80, 80), font=font_regular)

    return canvas

def create_composite(nova_path, background_path, output_path, nova_scale=0.4, flip_nova=False):
    """Create a composite image with Nova on left and background on right."""
    # Load images
    nova = Image.open(nova_path).convert("RGBA")
    background = Image.open(background_path).convert("RGBA")

    # Flip Nova horizontally if needed (to point right instead of left)
    if flip_nova:
        nova = ImageOps.mirror(nova)

    # Create canvas (1920x1080)
    canvas = Image.new("RGBA", (1920, 1080), (255, 255, 255, 255))

    # Resize background to fit right 65% of frame
    bg_width = int(1920 * 0.65)
    bg_height = 1080
    background = background.resize((bg_width, bg_height), Image.LANCZOS)

    # Paste background on right side
    canvas.paste(background, (1920 - bg_width, 0))

    # Resize Nova to fit left side
    nova_height = int(1080 * nova_scale)
    nova_ratio = nova.width / nova.height
    nova_width = int(nova_height * nova_ratio)
    nova = nova.resize((nova_width, nova_height), Image.LANCZOS)

    # Position Nova on left bottom
    nova_x = 50
    nova_y = 1080 - nova_height - 20

    # Paste Nova with transparency
    canvas.paste(nova, (nova_x, nova_y), nova)

    # Add logo to top-left corner
    canvas = add_logo(canvas)

    # Convert to RGB and save
    canvas_rgb = canvas.convert("RGB")
    canvas_rgb.save(output_path, quality=95)
    print(f"Created: {output_path}")

def resize_to_1920x1080(input_path, output_path):
    """Resize an image to 1920x1080 and add logo."""
    img = Image.open(input_path).convert("RGBA")
    img = img.resize((1920, 1080), Image.LANCZOS)
    # Add logo to top-left corner
    img = add_logo(img)
    img_rgb = img.convert("RGB")
    img_rgb.save(output_path, quality=95)
    print(f"Resized with logo: {output_path}")

# View 1: Question screen ALREADY has Nova waving - just resize
resize_to_1920x1080(
    f"{ASSETS_DIR}/screen_question.png",
    f"{ASSETS_DIR}/view1.png"
)

# Scene 2: Original pointing (flipped to point RIGHT) + Empty Desmos
create_composite(
    f"{ASSETS_DIR}/nova_pointing.png",  # Original with correct glasses
    f"{DESMOS_DIR}/desmos_01_empty.png",
    f"{ASSETS_DIR}/view2.png",
    nova_scale=0.7,
    flip_nova=True  # Flip to point right
)

# Scene 3: Original pointing (flipped to point RIGHT) + y=4x graphed
create_composite(
    f"{ASSETS_DIR}/nova_pointing.png",
    f"{DESMOS_DIR}/desmos_02_y_equals_4x.png",
    f"{ASSETS_DIR}/view3.png",
    nova_scale=0.7,
    flip_nova=True
)

# Scene 4: Original pointing (flipped to point RIGHT) + Both equations
create_composite(
    f"{ASSETS_DIR}/nova_pointing.png",
    f"{DESMOS_DIR}/desmos_03_both_equations.png",
    f"{ASSETS_DIR}/view4.png",
    nova_scale=0.7,
    flip_nova=True
)

# Scene 5: Thinking + Zoomed intersections
create_composite(
    f"{ASSETS_DIR}/nova_thinking.png",
    f"{DESMOS_DIR}/desmos_04_zoomed_intersections.png",
    f"{ASSETS_DIR}/view5.png",
    nova_scale=0.7,
    flip_nova=False  # Thinking doesn't need flip
)

# Scene 6: Original pointing (flipped to point RIGHT) + Point highlighted
create_composite(
    f"{ASSETS_DIR}/nova_pointing.png",
    f"{DESMOS_DIR}/desmos_05_intersection_highlighted.png",
    f"{ASSETS_DIR}/view6.png",
    nova_scale=0.7,
    flip_nova=True
)

# View 7: Answer screen ALREADY has Nova celebrating - just resize
resize_to_1920x1080(
    f"{ASSETS_DIR}/screen_answer.png",
    f"{ASSETS_DIR}/view7.png"
)

print("\nAll 7 view images created!")
print("- Views 1 & 7: Use existing screens with Nova already present")
print("- Views 2-6: Original Nova pointing (flipped to point right) with correct glasses")
