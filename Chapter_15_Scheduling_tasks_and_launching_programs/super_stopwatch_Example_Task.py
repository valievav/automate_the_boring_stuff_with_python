'''
Say you want to track how much time you spend on boring tasks you haven’t automated yet.
At a high level, here’s what program should do:
• Track the amount of time elapsed between presses of the enter key, with each key press starting a new “lap” on the timer.
• Print the lap number, total time, and lap time
'''


import time


def stopwatch():

    number_of_launches = 0
    total_runtime = 0

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

            print(f"Statistic run:\n"
                  f"    number of launches = {number_of_launches},\n"
                  f"    total time = {total_runtime},\n"
                  f"    last run time = {run_time}")

    except KeyboardInterrupt:
        print("Exiting the program")
        exit()
        # note: to be able to terminate the stopwatch, run program in cmd
        # IDE(PyCharm) interferes and treats Ctrl+C as copy, so program run in IDE does not reach KeyboardInterrupt


stopwatch()







