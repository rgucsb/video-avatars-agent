#!/usr/bin/env python3
"""Create question and answer screens for the math video."""

from PIL import Image, ImageDraw, ImageFont
import os

ASSETS_DIR = "assets"
OUTPUT_DIR = "assets"

# Try to use a nice font, fall back to default
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


def create_question_screen(nova_path: str, output_path: str):
    """Create question screen with Nova and the math problem."""

    target_width = 1920
    target_height = 1080

    # Create white background
    img = Image.new("RGB", (target_width, target_height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Load Nova
    nova = Image.open(nova_path).convert("RGBA")

    # Resize Nova to fit left 30% of frame
    nova_target_width = int(target_width * 0.28)
    nova_ratio = nova_target_width / nova.width
    nova_new_height = int(nova.height * nova_ratio)

    max_nova_height = int(target_height * 0.85)
    if nova_new_height > max_nova_height:
        nova_ratio = max_nova_height / nova.height
        nova_new_height = max_nova_height
        nova_target_width = int(nova.width * nova_ratio)

    nova_resized = nova.resize((nova_target_width, nova_new_height), Image.Resampling.LANCZOS)

    # Position Nova on the left
    nova_x = int(target_width * 0.02)
    nova_y = target_height - nova_new_height - int(target_height * 0.05)
    img.paste(nova_resized, (nova_x, nova_y), nova_resized)

    # Draw question box on the right
    box_left = int(target_width * 0.35)
    box_top = int(target_height * 0.08)
    box_right = int(target_width * 0.95)
    box_bottom = int(target_height * 0.92)

    # Draw rounded rectangle background
    draw.rounded_rectangle(
        [box_left, box_top, box_right, box_bottom],
        radius=20,
        fill=(248, 249, 250),
        outline=(200, 200, 200),
        width=2
    )

    # Fonts
    title_font = get_font(36)
    equation_font = get_font(48)
    text_font = get_font(32)
    choice_font = get_font(36)

    # Draw "SAT Math" header
    header_y = box_top + 30
    draw.text((box_left + 40, header_y), "SAT Math - System of Equations", fill=(100, 100, 100), font=title_font)

    # Draw horizontal line
    line_y = header_y + 60
    draw.line([(box_left + 40, line_y), (box_right - 40, line_y)], fill=(200, 200, 200), width=2)

    # Draw equations
    eq_y = line_y + 40
    draw.text((box_left + 80, eq_y), "y = 4x", fill=(0, 0, 0), font=equation_font)
    draw.text((box_left + 80, eq_y + 70), "y = x² − 12", fill=(0, 0, 0), font=equation_font)

    # Draw question text
    q_y = eq_y + 180
    question_lines = [
        "A system of two equations is shown.",
        "If (x, y) is a solution to the system",
        "and x > 0, what is the value of x?"
    ]
    for i, line in enumerate(question_lines):
        draw.text((box_left + 40, q_y + i * 45), line, fill=(0, 0, 0), font=text_font)

    # Draw answer choices
    choices_y = q_y + 180
    choices = [
        ("A)", "−3"),
        ("B)", "4"),
        ("C)", "6"),
        ("D)", "12")
    ]

    for i, (letter, value) in enumerate(choices):
        choice_y = choices_y + i * 70
        # Draw choice circle
        circle_x = box_left + 60
        circle_r = 20
        draw.ellipse(
            [circle_x - circle_r, choice_y - circle_r + 18,
             circle_x + circle_r, choice_y + circle_r + 18],
            outline=(100, 100, 100),
            width=2
        )
        draw.text((circle_x - 10, choice_y), letter[0], fill=(100, 100, 100), font=choice_font)
        draw.text((circle_x + 50, choice_y), value, fill=(0, 0, 0), font=choice_font)

    img.save(output_path, "JPEG", quality=95)
    print(f"Created: {output_path}")


def create_answer_screen(nova_path: str, output_path: str):
    """Create answer screen with correct choice selected."""

    target_width = 1920
    target_height = 1080

    # Create white background
    img = Image.new("RGB", (target_width, target_height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Load Nova (celebrating)
    nova = Image.open(nova_path).convert("RGBA")

    # Resize Nova
    nova_target_width = int(target_width * 0.28)
    nova_ratio = nova_target_width / nova.width
    nova_new_height = int(nova.height * nova_ratio)

    max_nova_height = int(target_height * 0.85)
    if nova_new_height > max_nova_height:
        nova_ratio = max_nova_height / nova.height
        nova_new_height = max_nova_height
        nova_target_width = int(nova.width * nova_ratio)

    nova_resized = nova.resize((nova_target_width, nova_new_height), Image.Resampling.LANCZOS)

    # Position Nova
    nova_x = int(target_width * 0.02)
    nova_y = target_height - nova_new_height - int(target_height * 0.05)
    img.paste(nova_resized, (nova_x, nova_y), nova_resized)

    # Draw question box
    box_left = int(target_width * 0.35)
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
    title_font = get_font(36)
    equation_font = get_font(48)
    text_font = get_font(32)
    choice_font = get_font(36)
    correct_font = get_font(42)

    # Draw header
    header_y = box_top + 30
    draw.text((box_left + 40, header_y), "SAT Math - System of Equations", fill=(100, 100, 100), font=title_font)

    # Draw line
    line_y = header_y + 60
    draw.line([(box_left + 40, line_y), (box_right - 40, line_y)], fill=(200, 200, 200), width=2)

    # Draw equations
    eq_y = line_y + 40
    draw.text((box_left + 80, eq_y), "y = 4x", fill=(0, 0, 0), font=equation_font)
    draw.text((box_left + 80, eq_y + 70), "y = x² − 12", fill=(0, 0, 0), font=equation_font)

    # Draw question
    q_y = eq_y + 180
    question_lines = [
        "A system of two equations is shown.",
        "If (x, y) is a solution to the system",
        "and x > 0, what is the value of x?"
    ]
    for i, line in enumerate(question_lines):
        draw.text((box_left + 40, q_y + i * 45), line, fill=(0, 0, 0), font=text_font)

    # Draw answer choices with C selected
    choices_y = q_y + 180
    choices = [
        ("A)", "−3", False),
        ("B)", "4", False),
        ("C)", "6", True),  # Correct answer!
        ("D)", "12", False)
    ]

    for i, (letter, value, is_correct) in enumerate(choices):
        choice_y = choices_y + i * 70
        circle_x = box_left + 60
        circle_r = 20

        if is_correct:
            # Green filled circle for correct answer
            draw.ellipse(
                [circle_x - circle_r, choice_y - circle_r + 18,
                 circle_x + circle_r, choice_y + circle_r + 18],
                fill=(34, 197, 94),
                outline=(22, 163, 74),
                width=3
            )
            # White checkmark or letter
            draw.text((circle_x - 10, choice_y), letter[0], fill=(255, 255, 255), font=choice_font)
            draw.text((circle_x + 50, choice_y), value, fill=(34, 197, 94), font=correct_font)

            # Draw "Correct!" label
            draw.text((circle_x + 130, choice_y), "✓ Correct!", fill=(34, 197, 94), font=correct_font)
        else:
            # Gray circle for other choices
            draw.ellipse(
                [circle_x - circle_r, choice_y - circle_r + 18,
                 circle_x + circle_r, choice_y + circle_r + 18],
                outline=(180, 180, 180),
                width=2
            )
            draw.text((circle_x - 10, choice_y), letter[0], fill=(180, 180, 180), font=choice_font)
            draw.text((circle_x + 50, choice_y), value, fill=(150, 150, 150), font=choice_font)

    img.save(output_path, "JPEG", quality=95)
    print(f"Created: {output_path}")


def main():
    # Create question screen with Nova waving
    create_question_screen(
        os.path.join(ASSETS_DIR, "nova_waving.png"),
        os.path.join(OUTPUT_DIR, "screen_question.png")
    )

    # Create answer screen with Nova celebrating
    create_answer_screen(
        os.path.join(ASSETS_DIR, "nova_excited_celebrating.png"),
        os.path.join(OUTPUT_DIR, "screen_answer.png")
    )

    print("\nDone! Created question and answer screens.")


if __name__ == "__main__":
    main()
