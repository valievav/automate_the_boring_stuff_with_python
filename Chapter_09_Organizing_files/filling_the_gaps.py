#! python3

'''
Write a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert gaps
into numbered files so that a new file can be added.
'''

import os, shutil, re
from filling_the_gaps_file_generator import generate_files
from filling_the_gaps_gaps_creator import create_gaps


def fill_the_gaps(working_dir, prefix_to_find):
    file_list = os.listdir(working_dir)
    file_regex = re.compile(r"^" + re.escape(prefix_to_find) + r"((\d){3})(.txt)")
    count = 1  # var to check the files order

    for file in file_list:

        if file_regex.search(file):
            regex_number = file_regex.search(file).group(1)  # extracting the number from file name
            if int(regex_number.lstrip("0")) == count:  # check whether number in file is the same as count
                print(f"'{file}' file order is correct")
                count += 1
            else:
                order_number = str(count).zfill(3)  # forming correct order number for the file
                print(f"Found a gap! '{file}' should have {order_number} number. Doing the fix...")
                new_file_name = file.replace(regex_number, order_number)  # forming correct file name
                file_path_before = os.path.join(working_dir, file)
                file_path_after = os.path.join(working_dir, new_file_name)
                shutil.move(file_path_before, file_path_after)  # renaming file
                print(f"--> File {file_path_before} renamed to {file_path_after}")
                count += 1

        else:
            print(f"{file} nas no regex match")

    print("Done.")


path = "D:\\Filling gaps folder"
prefix = "spam"

# if folder is empty, fill it in with test data and create a gap
if not os.listdir(path):
    generate_files(path, 10)
    create_gaps(path)


# fill the gaps in files list
fill_the_gaps(path, prefix)

