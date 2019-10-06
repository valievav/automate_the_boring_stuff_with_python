'''
Write program that does next:
• Counts down time.
• Plays a sound file when the countdown reaches zero.
'''

import time, os, subprocess


def countdown(seconds, cwd=None):
    """
    Counts down seconds and runs music track when the countdown reaches zero.
    :param seconds: int
    :param cwd: absolute path, optional
    :return:
    """

    # change cwd if provided
    if cwd:
        os.chdir(cwd)

    # counting down seconds
    for second in range(seconds+1):
        if second == seconds:
            subprocess.Popen(['start', 'Synthworld.mp3'], shell=True)  # play music on the last second
        else:
            time.sleep(1)  # sleep until the last sec
            print(seconds-second)


time_seconds = 5
countdown(time_seconds)

