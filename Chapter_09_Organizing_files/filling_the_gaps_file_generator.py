#! python3
# This is ad additional module to the filling_the_gaps solution, that generates test files

import os


def generate_files(path, files_count):
    """
    Generates test files for filling_the_gaps.py task.\n
    All files have txt extension, start from "spam"  prefix and followed by 3 numbers generated in asc order
    (e.g., spam001.txt, spam002.txt)\n
    :param path: absolute path
    :param files_count: int
    :return: nothing
    """

    if not os.path.abspath(path):
        print("Only absolute path accepted")
        return

    for i in range(1, files_count+1):
        file_number = str(i).zfill(3)
        file_extension = ".txt"
        file_path = os.path.join(path, "spam" + file_number + file_extension)
        file = open(file_path, "w")
        file.write(f"Agent {file_number} file")
        file.close()


# runs only for this module
if __name__ == "__main__":
    working_dir = "D:\\Filling gaps folder"
    generate_files(working_dir, 3)
