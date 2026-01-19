def draw_line(tick_length: int, tick_label: str = ""):
    """Draw one line with given tick length (followed by optional label)"""
    line = "-" * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)


def draw_interval(center_length: int):
    """Draw tick interval based on Center tick length"""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches: int, major_length: int):
    """Draw English ruler with given number of inches and major tick length"""
    draw_line(major_length, "0")  # draw 0 line
    for j in range(1, num_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


if __name__ == "__main__":
    num_inches = 5
    major_length = 5
    draw_ruler(num_inches=num_inches, major_length=major_length)
