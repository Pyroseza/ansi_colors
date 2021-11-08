#!/usr/bin/env python3

# prints all ANSI colors codes in various sequence orders
# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors

import sys


def get_ansi_color(color: int, fgbg: int):
    return f"\033[{fgbg};5;{color}m  {color: ^3}  \033[0m"


def get_cube_coord(r: int, g: int, b: int):
    def is_valid(x: int, n: str):
        if not 0 <= x < 6:
            raise ValueError(f"{n} range outside of 0 <= x < 6")

    is_valid(r, "Red")
    is_valid(g, "Green")
    is_valid(b, "Blue")
    return 16 + (36 * r) + (6 * g) + b


def cube_colors(order: str = None):
    default_order = "rbg"
    if not order or len(order) != 3 or sorted(order) != sorted(default_order):
        order = default_order
        print(f"  Invalid order, defaulting to {order}\n")
    for a in range(6):
        for b in range(6):
            for c in range(6):
                rgb = dict(zip(order, [a, b, c]))
                yield get_cube_coord(**rgb)


def main(order: str = None):
    for fb, title in ((38, "Foreground"), (48, "Background")):  # Foreground and Background values
        print(f"{title}\n")
        # ANSI colors
        for color in range(16):  # Colors from 0 to 15
            if color == 0:
                print("  Standard colors")
            elif color == 8:
                print("  High-intensity colors")
            end = "\n" if (color + 1) % 8 == 0 else ""
            print(get_ansi_color(color, fb), end=end)
        print(f"\n  216 colors - cube (order = {order})")
        for i, color in enumerate(cube_colors(order)):  # Colors from 16 to 2321
            # Display the color
            end = "\n" if (i + 1) % 6 == 0 else ""
            print(get_ansi_color(color, fb), end=end)
        print("\n  Greyscale colors")
        for color in range(232, 256):  # Colors from 232 to 255
            end = "\n" if (color + 1) % 8 == 0 else ""
            print(get_ansi_color(color, fb), end=end)
        print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
