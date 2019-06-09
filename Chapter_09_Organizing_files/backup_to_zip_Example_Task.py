#! python3
# backup_to_zip_Example_Task.py - creates backup of a folder with all its content
# NOTE: This solution is quite different from the book (major one being better backup number detection).

import os, re, zipfile


def create_zip_backup(folder_path):
    """
    Creates zip archive for the folder specified in the param.\n
    The archive name consists of the original folder name plus an incremental number,
    which displays the number of the archive in the folder.\n
    :param folder_path:
    :return: nothing
    """

    # checking that parameter contains absolute path
    if not os.path.isabs(folder_path):
        print("Required an absolute path to generate a zip backup")
        return

    # checking that folder exists before backuping
    if not os.path.isdir(folder_path):
        print(f"Folder '{folder_path}' doesn't exist")
        return

    # retrieving cwd and name of the folder
    folder_name = os.path.basename(folder_path)
    cwd = os.path.dirname(folder_path)
    os.chdir(cwd)
    print(f"Current working directory - '{cwd}'\nFolder to be archived - '{folder_name}'")

    # regex to find existing archives with the same name as the folder
    zip_regex = re.compile(r"{0}(_)?(\d)*?(.zip)$".format(folder_name))
    max_zip_number = 0

    # searching for max zip number to increase it during backup creation
    for item in os.listdir(cwd):
        if zip_regex.search(item):
            zip_number_part = re.search(r"(\d+)(.zip)$", zip_regex.search(item).group())

            # max number ensures count consistency (if some archive is removed, it's number won't be taken)
            if int(zip_number_part[1]) > max_zip_number:
                max_zip_number = int(zip_number_part[1])

    archive_name = "_".join([folder_name, str(max_zip_number+1)]) + ".zip"
    print(f"Max number of existing archive - {max_zip_number}")

    # creating zip folder
    archive = zipfile.ZipFile(archive_name, "w")
    print(f"Created '{archive_name}'.\nGoing to populate archive:")

    subfolders_count = 0
    files_count = 0

    # populating backup's files and subfolders
    for current_folder, subfolders, files in os.walk(folder_path):
        print(f"{' '*3}Populating {current_folder}...")

        for item in subfolders:
            subfolder_path = os.path.join(current_folder, item)
            archive.write(subfolder_path, compress_type=zipfile.ZIP_DEFLATED)
            subfolders_count += 1

        for item in files:
            file_path = os.path.join(current_folder, item)
            archive.write(file_path, compress_type=zipfile.ZIP_DEFLATED)
            files_count += 1

    print(f"Done. Backup '{archive_name}' is complete.\n"
          f"Backup SUMMARY: total number of subfolders - {subfolders_count}, total number of files - {files_count}.")

    archive.close()


# specifying abs path to original folder
user_folder_path = "D:\\Service_usage_statistic_2019"

# creating zip backup for specified folder
create_zip_backup(user_folder_path)


