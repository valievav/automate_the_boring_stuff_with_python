#! python3
# rename_dates_Example_Task.py - Renames American-style dates (MM-DD-YYYY) in files to European-style dates (DD-MM-YYYY)

# NOTE: This solution takes completely different approach from the book's solution
# PRE-CONDITION: assumption that file scope doesn't have DD-MM-YYYY format in names, only american style, some numbers and other date styles
# The reason being if files have DD-MM-YYYY mixed in, it would require user input or advanced logic to resolve dates like 01-03-2010

import shutil, os, re
from rename_dates_files_generator import generate_files


def rename_date_formats(files_list):
    """
    Renames American style dates (MM-DD-YYYY) in files to European format (DD-MM-YYYY) and prints results to the console\n
    Input - files_list\nOutput - nothing
    """

    count_renamed = 0
    count_skipped = 0

    for file in files_list:

        # finding DD-DD-DDDD matches
        if date_regex.search(file):
            date_format = date_regex.search(file).group()
            date_split = date_format.split("-")

            # detecting MM-DD-YYYY format and renaming to DD-MM-YYYY format
            if 1 <= int(date_split[0]) <= 12 and 1 <= int(date_split[1]) <= 31:
                european_format_date = "-".join([date_split[1], date_split[0], date_split[2]])
                new_file_name = file.replace(date_format, european_format_date)

                # checking that newly renamed file won't be a duplicate
                if new_file_name not in files_list:
                    shutil.move(file, new_file_name)
                    print(f"<{file}> renamed to <{new_file_name}>")
                    count_renamed += 1
                else:
                    print(f"Cannot rename <{file}> because file <{new_file_name}> already exists")
                    count_skipped += 1

            # for files with DD-DD-DDDD format, but not MM-DD-YYYY like 89-77-3445
            else:
                print(f"<{file}> has no MM-DD-YYYY date in name")
                count_skipped += 1

        # for files with no MM-DD-YYYY format like 12-1221.txt or text.pdf
        else:
            print(f"<{file}> has no MM-DD-YYYY date in name")
            count_skipped += 1

    print(f"\nSUMMARY:\nRenamed files count - {count_renamed}, not affected files count - {count_skipped}.")


cwd = "D:\\Service_usage_statistic_2019"
os.chdir(cwd)

# populating cwd folder with example files if it's empty
if not os.listdir(cwd):
    generate_files()

# regex to detect DD-DD-DDDD format
date_regex = re.compile(r"(\d{2})(-)(\d{2})(-)(\d{4})")

# detecting and renaming american style dates to european style dates
rename_date_formats(os.listdir(cwd))

