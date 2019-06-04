#! python3
# rename_dates_files_generator.py - Generates files with American style date MM-DD-YYYY and files with MM-YYYY
# (as a negative case for rename_dates_Example_task.py)


def generate_files():

    for month in range(1, 13):
        month_str = str(month).zfill(2)  # adding leading zeros to 1-9 months
        files = []
        files += [f"'Ice Dragon' launches statistic {month_str}-25-2019.pdf"]  # date in the end
        files += [f"{month_str}-25-2019 'Ice Dragon' launches breakdown.xlsx"]  # date in the middle
        files += [f"Monthly supply summary as of {month_str}-25-2019.docx"]  # date in the beginning
        files += [f"{month_str}-2019 starship re-supply list.txt"]  # MM-YYYY date format (negative case)

        for file in files:
            new_file = open(file, "w")
            new_file.close()


# run this method only directly, not through import
if __name__ == "__main__":
    import os
    os.chdir("D:\\Service_usage_statistic_2019")
    generate_files()
