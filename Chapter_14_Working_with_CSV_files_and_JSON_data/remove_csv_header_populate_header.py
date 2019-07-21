import csv, os


def create_csv_file(cwd=None, file_name_prefix=None, header_data=None, file_data=None):
    """
    Creates csv files with values and header data.\n
    This is a supportive program to the main remove_csv_header_Example_Task.py\n
    :param cwd: absolute path, optional (used cwd if not passed)
    :param file_name_prefix: str, optional (used default value if not passed)
    :param header_data: list, optional (used default value if not passed)
    :param file_data: list, optional (used default value if not passed)
    :return: None
    """

    # populating params if they're None
    if not file_name_prefix:
        file_name_prefix = "remove_csv_header_file"

    if not header_data:
        header_data = ["Episode Number", "Episode Name"]

    if not file_data:
        file_data = [["The Vanishing of Will Byers", "The Weirdo on Maple Street", "Holly, Jolly", "The Body",
                      "The Flea and the Acrobat", "The Monster", "The Bathtub", "The Upside Down"],
                     ["MADMAX", "Trick or Treat, Freak", "The Pollywog", "Will the Wise", "Dig Dug",
                      "The Spy", "The Lost Sister", "The Mind Flayer", "The Gate"],
                     ["Suzie, Do You Copy?", "The Malls Rats", "The Case of the Missing Lifeguard", "The Sauna Test",
                      "The Flayed", "E Pluribus Unum", "The Bite", "The Battle of Starcourt"]]

    # switching to specified cwd
    if cwd:
        os.chdir(cwd)

    # create file
    for number in range(len(file_data)):
        file_name = f"{file_name_prefix}{number+1}.csv"
        file_obj = open(file_name, "w", newline='')
        writer = csv.writer(file_obj)

        # write header data
        writer.writerow(header_data)

        # write main data
        for value_number in range(len(file_data[number])):
            writer.writerow([value_number+1, file_data[number][value_number]])
        file_obj.close()
        print(f"Created file '{file_name}'")


# run only for this module
if __name__ == "__main__":
    working_directory = "D:\\Chapter_14"
    create_csv_file(working_directory)

