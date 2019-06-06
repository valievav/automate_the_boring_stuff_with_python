#! python3

'''
Write a program that walks through a folder tree and searches for exceptionally
large files or folders—say, ones that have a file size of more than
100MB. (Remember, to get a file’s size, you can use os.path.getsize() from
the os module.) Print these files with their absolute path to the screen.

NOTE: solution was improved to display files sorted by size
'''


import os
from sorting_file_size_solutions import sort_results_by_size  # module with several solution to sorting list problem


def find_files_greater_than_threshold(path, threshold_file_size):
    """
    Finds files that are >= threshold size and prints results sorted by the file size in desc order.\n
    :param path: absolute path
    :param threshold_file_size: int value
    :return: nothing
    """

    if not os.path.isabs(path):
        print("Specified path should be absolute")
        return

    files_list_result = []  # store detected files and sizes to later sort by size

    # iterate through each file and store those that meet the size requirement
    for active_folder, subfolder, files in os.walk(path):
        print(f"Searching in folder {active_folder}")

        for item in files:
            item_path = os.path.join(active_folder, item)

            try:
                item_size = os.path.getsize(item_path)
            except OSError:
                print(f"File {item} cannot be accessed")  # some files can be unavailable for check
            else:
                if item_size >= threshold_file_size:
                    files_list_result.append([item_path, item_size])

    # sort list by size (to change sorting solution, head over to solutions module)
    sorted_results, list_length = sort_results_by_size(files_list_result)

    print(f"SUMMARY: Found {list_length} files >= {threshold_file_size}:")
    for file, size in sorted_results:
        print(str(size).ljust(10), str(file).ljust(100))


search_path = "D:\\Jupyter notebook"
user_threshold_file_size = 4000

find_files_greater_than_threshold(search_path, user_threshold_file_size)

