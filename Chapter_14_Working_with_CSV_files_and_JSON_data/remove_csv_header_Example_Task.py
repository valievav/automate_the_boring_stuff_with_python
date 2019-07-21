import csv, os
from remove_csv_header_populate_header import create_csv_file


def remove_csv_header(cwd=None, files_name_prefix=None):
    """
    Removes header data (first row) from csv files.\n
    :param files_name_prefix: string
    :param cwd: absolute path, optional param
    :return: None
    """

    # populating param if it's None
    if not files_name_prefix:
        files_name_prefix = "remove_csv_header_file"

    # switching to specified cwd
    if cwd:
        os.chdir(cwd)

    # go through all files in cwd
    files_list = os.listdir(".")
    for file in files_list:
        file_part = file.split(".")

        # find specific csv files
        if file_part[-1] == "csv" and file_part[0].startswith(files_name_prefix):
            # read file data
            csv_file = open(file)
            reader = csv.reader(csv_file)
            data = list(reader)

            # record the data into the same csv file
            csv_file = open(file, "w", newline='')
            writer = csv.writer(csv_file)

            # record the data except the 1st row
            for line in data[1:]:
                writer.writerow(line)
            csv_file.close()
            print(f"Removed header from '{file}'")


working_dir = "D:\\Chapter_14"

create_csv_file()
remove_csv_header()

