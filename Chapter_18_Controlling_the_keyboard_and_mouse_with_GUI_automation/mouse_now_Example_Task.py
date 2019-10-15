"""
Write a program that constantly displays the x- and y-coordinates of the
mouse cursor as you move it around.
"""
import pyautogui
import sys


def display_mouse_position():
    print("Press Ctrl+C to interrupt the program")
    x_prev, y_prev = 0, 0
    line_len = 0

    try:
        while True:
            x_new, y_new = pyautogui.position()

            # print new position only if it was changed
            if x_new != x_prev and y_new != y_prev:
                print("\b"*line_len, end="")  # erase previously printed line

                result_line = f"x = {x_new}, y = {y_new}"
                print(result_line, end="")
                x_prev, y_prev, line_len = x_new, y_new, len(result_line)

    # note: to be able to terminate program, run it in cmd
    # IDE(PyCharm) interferes and treats Ctrl+C as copy, so program run in IDE never reaches KeyboardInterrupt
    except KeyboardInterrupt:
        print("\nProgram finished")  # interrupt on Ctrl+C
        sys.exit()


if __name__ == "__main__":
    display_mouse_position()

