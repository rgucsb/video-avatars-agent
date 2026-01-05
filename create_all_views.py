#!/usr/bin/env python3
"""Create all view images for the complete SAT math tutorial."""

from PIL import Image, ImageDraw, ImageFont
import os

ASSETS_DIR = "assets"
DESMOS_DIR = "assets/desmos"
OUTPUT_DIR = "assets"

def get_font(size):
    fonts_to_try = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSText.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for font_path in fonts_to_try:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except:
                pass
    return ImageFont.load_default()


def create_composite(nova_path: str, background_path: str, output_path: str, nova_scale=0.28):
    """Create a composite image with Nova on the left and background on the right."""

    target_width = 1920
    target_height = 1080

    # Create white background
    composite = Image.new("RGBA", (target_width, target_height), (255, 255, 255, 255))

    # Load background (Desmos screenshot or question screen)
    bg = Image.open(background_path).convert("RGBA")

    # Resize background to fit right 65% of frame
    bg_target_width = int(target_width * 0.65)
    bg_ratio = bg_target_width / bg.width
    bg_new_height = int(bg.height * bg_ratio)

    if bg_new_height > target_height:
        bg_ratio = target_height / bg.height
        bg_new_height = target_height
        bg_target_width = int(bg.width * bg_ratio)

    bg_resized = bg.resize((bg_target_width, bg_new_height), Image.Resampling.LANCZOS)

    # Position background on the right side
    bg_x = target_width - bg_target_width
    bg_y = (target_height - bg_new_height) // 2
    composite.paste(bg_resized, (bg_x, bg_y), bg_resized)

    # Load Nova
    nova = Image.open(nova_path).convert("RGBA")

    # Resize Nova
    nova_target_width = int(target_width * nova_scale)
    nova_ratio = nova_target_width / nova.width
    nova_new_height = int(nova.height * nova_ratio)

    max_nova_height = int(target_height * 0.9)
    if nova_new_height > max_nova_height:
        nova_ratio = max_nova_height / nova.height
        nova_new_height = max_nova_height
        nova_target_width = int(nova.width * nova_ratio)

    nova_resized = nova.resize((nova_target_width, nova_new_height), Image.Resampling.LANCZOS)

    # Position Nova on the left side
    nova_x = int(target_width * 0.02)
    nova_y = target_height - nova_new_height - int(target_height * 0.05)

    composite.paste(nova_resized, (nova_x, nova_y), nova_resized)

    # Convert to RGB and save as PNG (better quality for starting frames)
    composite_rgb = composite.convert("RGB")
    composite_rgb.save(output_path, "PNG")
    print(f"Created: {output_path}")


def create_question_screen(output_path: str):
    """Create standalone question screen."""
    target_width = 1920
    target_height = 1080

    img = Image.new("RGB", (target_width, target_height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Draw question box
    box_left = int(target_width * 0.05)
    box_top = int(target_height * 0.08)
    box_right = int(target_width * 0.95)
    box_bottom = int(target_height * 0.92)

    draw.rounded_rectangle(
        [box_left, box_top, box_right, box_bottom],
        radius=20,
        fill=(248, 249, 250),
        outline=(200, 200, 200),
        width=2
    )

    # Fonts
    title_font = get_font(42)
    equation_font = get_font(56)
    text_font = get_font(36)
    choice_font = get_font(42)

    # Draw header
    header_y = box_top + 40
    draw.text((box_left + 60, header_y), "SAT Math - System of Equations", fill=(80, 80, 80), font=title_font)

    # Draw line
    line_y = header_y + 70
    draw.line([(box_left + 60, line_y), (box_right - 60, line_y)], fill=(200, 200, 200), width=2)

    # Draw equations (centered)
    eq_y = line_y + 60
    draw.text((target_width // 2 - 100, eq_y), "y = 4x", fill=(0, 0, 0), font=equation_font)
    draw.text((target_width // 2 - 150, eq_y + 80), "y = x² − 12", fill=(0, 0, 0), font=equation_font)

    # Draw question
    q_y = eq_y + 200
    question_lines = [
        "A system of two equations is shown.",
        "If (x, y) is a solution to the system and x > 0,",
        "what is the value of x?"
    ]
    for i, line in enumerate(question_lines):
        draw.text((box_left + 60, q_y + i * 50), line, fill=(0, 0, 0), font=text_font)

    # Draw answer choices
    choices_y = q_y + 200
    choices = [("A)", "−3"), ("B)", "4"), ("C)", "6"), ("D)", "12")]

    for i, (letter, value) in enumerate(choices):
        choice_y = choices_y + i * 80
        circle_x = box_left + 100
        circle_r = 24
        draw.ellipse(
            [circle_x - circle_r, choice_y - circle_r + 20,
             circle_x + circle_r, choice_y + circle_r + 20],
            outline=(100, 100, 100),
            width=2
        )
        draw.text((circle_x - 12, choice_y), letter[0], fill=(100, 100, 100), font=choice_font)
        draw.text((circle_x + 60, choice_y), value, fill=(0, 0, 0), font=choice_font)

    img.save(output_path, "PNG")
    print(f"Created: {output_path}")


def create_answer_screen(output_path: str):
    """Create standalone answer screen with correct choice."""
    target_width = 1920
    target_height = 1080

    img = Image.new("RGB", (target_width, target_height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Draw question box
    box_left = int(target_width * 0.05)
    box_top = int(target_height * 0.08)
    box_right = int(target_width * 0.95)
    box_bottom = int(target_height * 0.92)

    draw.rounded_rectangle(
        [box_left, box_top, box_right, box_bottom],
        radius=20,
        fill=(248, 249, 250),
        outline=(200, 200, 200),
        width=2
    )

    # Fonts
    title_font = get_font(42)
    equation_font = get_font(56)
    text_font = get_font(36)
    choice_font = get_font(42)
    correct_font = get_font(48)

    # Draw header
    header_y = box_top + 40
    draw.text((box_left + 60, header_y), "SAT Math - System of Equations", fill=(80, 80, 80), font=title_font)

    # Draw line
    line_y = header_y + 70
    draw.line([(box_left + 60, line_y), (box_right - 60, line_y)], fill=(200, 200, 200), width=2)

    # Draw equations
    eq_y = line_y + 60
    draw.text((target_width // 2 - 100, eq_y), "y = 4x", fill=(0, 0, 0), font=equation_font)
    draw.text((target_width // 2 - 150, eq_y + 80), "y = x² − 12", fill=(0, 0, 0), font=equation_font)

    # Draw question
    q_y = eq_y + 200
    question_lines = [
        "A system of two equations is shown.",
        "If (x, y) is a solution to the system and x > 0,",
        "what is the value of x?"
    ]
    for i, line in enumerate(question_lines):
        draw.text((box_left + 60, q_y + i * 50), line, fill=(0, 0, 0), font=text_font)

    # Draw answer choices with C selected
    choices_y = q_y + 200
    choices = [("A)", "−3", False), ("B)", "4", False), ("C)", "6", True), ("D)", "12", False)]

    for i, (letter, value, is_correct) in enumerate(choices):
        choice_y = choices_y + i * 80
        circle_x = box_left + 100
        circle_r = 24

        if is_correct:
            # Green filled circle
            draw.ellipse(
                [circle_x - circle_r, choice_y - circle_r + 20,
                 circle_x + circle_r, choice_y + circle_r + 20],
                fill=(34, 197, 94),
                outline=(22, 163, 74),
                width=3
            )
            draw.text((circle_x - 12, choice_y), letter[0], fill=(255, 255, 255), font=choice_font)
            draw.text((circle_x + 60, choice_y), value, fill=(34, 197, 94), font=correct_font)
            draw.text((circle_x + 150, choice_y), "✓ Correct!", fill=(34, 197, 94), font=correct_font)
        else:
            draw.ellipse(
                [circle_x - circle_r, choice_y - circle_r + 20,
                 circle_x + circle_r, choice_y + circle_r + 20],
                outline=(180, 180, 180),
                width=2
            )
            draw.text((circle_x - 12, choice_y), letter[0], fill=(180, 180, 180), font=choice_font)
            draw.text((circle_x + 60, choice_y), value, fill=(150, 150, 150), font=choice_font)

    img.save(output_path, "PNG")
    print(f"Created: {output_path}")


def main():
    # Create standalone screens first
    create_question_screen(os.path.join(OUTPUT_DIR, "bg_question.png"))
    create_answer_screen(os.path.join(OUTPUT_DIR, "bg_answer.png"))

    # Define all views for the complete tutorial
    # Format: (nova_image, background_image, output_name, description)
    views = [
        # Scene 1: Introduction - Nova waving with question
        ("nova_waving.png", "bg_question.png", "view1.png", "Intro: Waving + Question"),

        # Scene 2: Opening Desmos - Nova pointing at empty grid
        ("nova_pointing.png", "desmos/desmos_01_empty.png", "view2.png", "Empty Desmos grid"),

        # Scene 3: First equation - Nova pointing at y=4x
        ("nova_pointing.png", "desmos/desmos_02_y_equals_4x.png", "view3.png", "Desmos with y=4x"),

        # Scene 4: Both equations - Nova pointing at parabola
        ("nova_pointing.png", "desmos/desmos_03_both_equations.png", "view4.png", "Both equations"),

        # Scene 5: Finding intersection - Nova thinking
        ("nova_thinking.png", "desmos/desmos_04_zoomed_intersections.png", "view5.png", "Zoomed intersections"),

        # Scene 6: Highlighting point - Nova pointing at (6,24)
        ("nova_pointing.png", "desmos/desmos_05_intersection_highlighted.png", "view6.png", "Point (6,24) highlighted"),

        # Scene 7: Conclusion - Nova celebrating with answer
        ("nova_excited_celebrating.png", "bg_answer.png", "view7.png", "Answer: C) 6"),
    ]

    print("\nCreating all view images...")
    print("=" * 60)

    for nova_img, bg_img, output_name, description in views:
        nova_path = os.path.join(ASSETS_DIR, nova_img)
        bg_path = os.path.join(ASSETS_DIR, bg_img)
        output_path = os.path.join(OUTPUT_DIR, output_name)

        if not os.path.exists(nova_path):
            print(f"Warning: Nova image not found: {nova_path}")
            continue
        if not os.path.exists(bg_path):
            print(f"Warning: Background not found: {bg_path}")
            continue

        create_composite(nova_path, bg_path, output_path)
        print(f"  → {description}")

    print("=" * 60)
    print(f"\nDone! Created {len(views)} view images:")
    for _, _, output_name, description in views:
        print(f"  • {output_name}: {description}")


if __name__ == "__main__":
    main()
