#! python3

import os, random, send2trash


def create_gaps(path):
    """
    Removes random file from the folder
    :param path:
    :return:
    """
    random_file = random.choice(os.listdir(path))  # randomly selecting a file
    send2trash.send2trash(os.path.join(path, random_file))  # creating a gap in the list of files
    print(f"{random_file} is removed from the '{path}'")


# run from this module only
if __name__ == "__main__":
    working_dir = "D:\\Filling gaps folder"
    create_gaps(working_dir)
