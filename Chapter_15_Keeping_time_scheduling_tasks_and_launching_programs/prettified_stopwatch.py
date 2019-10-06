'''
Expand the previous stopwatch project so that it uses the rjust()
and ljust() string methods to “prettify” the output.
Next, use the pyperclip module to copy the text output to the clipboard
so the user can quickly paste the output to a text file or email.
'''

import time, pyperclip


def stopwatch():

    number_of_launches = 0
    total_runtime = 0
    result_lines = []

    try:

        while True:  # moved while statement inside of try-except so KeyboardInterrupt can be executed

            input("To start stopwatch press ENTER. To stop it press ENTER again. Press Ctrl+C to exit the program.\n")
            print("Stopwatch launched...")

            start = time.time()
            number_of_launches += 1

            input()
            print("Stopwatch is stopped.")
            end = time.time()
            run_time = round(end-start, 2)
            total_runtime = round(total_runtime + run_time, 2)

            # prettify output
            result_line = f"Lap #{str(number_of_launches).rjust(2)}: {str(total_runtime).rjust(5)} ({str(run_time).rjust(5)})"
            print(result_line)
            result_lines.append(result_line)

            if number_of_launches == 3:
                lines = "\n".join(result_lines)
                pyperclip.copy(lines)
                print(lines)

    except KeyboardInterrupt:
        print("Exiting the program")

        # copy results to clipboard
        lines = "\n".join(result_lines)
        pyperclip.copy(lines)
        print(lines)

        exit()
        # note: to be able to terminate the stopwatch, run program in cmd
        # IDE(PyCharm) interferes and treats Ctrl+C as copy, so program run in IDE does not reach KeyboardInterrupt


stopwatch()

