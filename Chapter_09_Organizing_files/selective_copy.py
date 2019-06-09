#! python3
# selective_copy - copies files with specified extension from a folder tree and copies them to the new folder

"""
Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from whatever
location they are into a new folder.
"""

import os, shutil


def selective_copy(original_path, destination_path, extensions):
    """
    Searches for files with specific extensions (e.g., pdf, txt") and moves them from original into destination directory.\n
    :param original_path: should be absolute, point to a directory and be existent
    :param destination_path: should be absolute and point to a directory (created if not exists)
    :param extensions: list of string values
    :return: nothing
    """
    # checking original folder path: should be absolute and a directory
    if not os.path.isabs(original_path):
        print("Original path should be an absolute.")
        return
    
    if not os.path.isdir(original_path):
        print("Original path  should be a directory.")
        return
    
    # checking destination folder path: should be absolute
    if not os.path.isabs(destination_path):
        print("Destination path should be absolute.")
        return
    
    # creating destination folder if absent
    try:
        if not os.path.exists(destination_path):
            os.mkdir(destination_path)
    except FileNotFoundError:
        print("Destination path should be a directory.")
        return


    print(f"Searching for files with {extensions} extensions in folder '{original_path}'.\n"
          f"Going to move files into '{destination_path}'")
    extensions_found = {}

    # searching for files and moving them into new directory
    for active_folder, subfolders, files in os.walk(original_path):
        print(f"    Processing '{active_folder}'...")
    
        # finding files with required extensions
        for item in files:
            if item.split(".")[-1] in extensions:
                file_ext = item.split(".")[-1]

                # counting founded files
                if file_ext in extensions_found.keys():
                    ext_count = extensions_found[file_ext] + 1
                    extensions_found[file_ext] = ext_count  # increasing count number for existing extension
                else:
                    ext_count = 1
                    extensions_found.setdefault(file_ext, ext_count)  # creating record for new extension

                # moving file into destination folder
                if item not in os.listdir(destination_path):
                    item_abs_path_before = os.path.join(active_folder, item)
                    item_abs_path_after = os.path.join(destination_path, item)
                    shutil.move(item_abs_path_before, item_abs_path_after)
                else:
                    print(f"Skipping file '{item}' since it already exists in the '{destination_path}'")
                    new_ext_count = extensions_found[file_ext] - 1  # subtracting skipped files count
                    extensions_found[file_ext] = new_ext_count

    # finding general number of moved files
    moved_files_count = 0
    for v in extensions_found.values():
        moved_files_count += v
    
    # print results
    print(f"Done. Moved {moved_files_count} file(s):", end="")
    for k, v in extensions_found.items():
        print(f" {k} - {v}", end="")


from_folder = "D:\\Service_usage_statistic_2019"
to_folder = "D:\\Selective_copy_results"
search_extensions = ['xlsx', 'docx']

selective_copy(from_folder, to_folder, search_extensions)
