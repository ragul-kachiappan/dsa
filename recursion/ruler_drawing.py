def draw_line(tick_length: int, tick_label: str = ""):
    """Draw one line with given tick length (followed by optional label.)"""
    line = "-" * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)


def draw_interval(center_length: int):
    """Draw tick interval based on central tick length."""
    if center_length > 0:  # stop when length drops to 0
        draw_interval(center_length - 1)  # recursively draw top ticks
        draw_line(center_length)  # draw center tick
        draw_interval(center_length - 1)  # recursively draw bottom ticks


def draw_ruler(num_inches: int, major_length: int):
    """Draw English Ruler with given number of inches, major tick length."""
    draw_line(major_length, "0")  # draw 0 inch line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)  # draw interior ticks for inch
        draw_line(major_length, str(j))  # draw inch j line  and label


if __name__ == "__main__":
    draw_ruler(10, 5)
