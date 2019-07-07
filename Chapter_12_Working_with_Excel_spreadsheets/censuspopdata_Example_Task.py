# NOTE: storing initial xlsx file and resulted py file in the same folder as a code for visibility

import openpyxl, pprint


def census_calc(file, county_column, population_column):
    """
    Counts both the total population and the number of census tracts\n
    for each county based on Excel xlsx data file.
    :param file: xlsx format
    :return: results are stored in censuspopdata_result.py
    """

    if not file.endswith(".xlsx"):
        print("File extension should be 'xlsx'. Please pass the file with the correct extension.")
        return

    # open Excel workbook
    try:
        wb = openpyxl.load_workbook(file)
    except FileNotFoundError:
        print("No such file. Please pass the existing file name.")
    else:
        sheet = wb.active

        # create a unique list of counties for storing results
        county_list = list(sheet.columns)[county_column-1]  # getting objects from column with county values
        unique_counties = {}

        for item in county_list[1:]:  # excluding header from the list of counties
            if item.value not in unique_counties:
                unique_counties.setdefault(item.value, {"number of tracts": 0, "population": 0})

        # go over each county and make calculations
        print("Running calculations for the county list...")

        for county in unique_counties.keys():
            for item in county_list:
                if county == item.value:
                    unique_counties[county]["number of tracts"] += 1
                    pop = sheet.cell(row=item.row, column=population_column).value
                    unique_counties[county]["population"] += pop

        # write results into a file
        result_file = open("censuspopdata_result.py", 'w')
        result_file.write(f"censuspopdata_result = {pprint.pformat(unique_counties)}")
        result_file.close()

        print("DONE.")


data_file = "censuspopdata_file.xlsx"
county_column_number = 3
population_column_number = 4
census_calc(data_file, county_column_number, population_column_number)

