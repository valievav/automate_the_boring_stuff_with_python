# NOTE: storing initial xlsx file and resulted py file in the same folder as a code for visibility

import openpyxl, pprint


def census_calc(file):
    """
    Counts both the total population and the number of census tracts\n
    for each county based on Excel data.
    :param file: Excel format
    :return: results are stored in censuspopdata_result.py
    """

    # open Excel workbook
    wb = openpyxl.load_workbook(file)
    sheet = wb.active

    # create a unique list of counties for storing results
    county_list = list(sheet.columns)[2]  # getting objects from column 2 with county values
    unique_counties = {}

    for item in county_list:
        if item.value not in unique_counties:
            unique_counties.setdefault(item.value, {"number of tracts": 0, "population": 0})

    del unique_counties["County"]  # removing header value from the county list

    # go over each county and make calculations
    print("Running calculations for the county list...")

    for county in unique_counties.keys():
        for item in county_list:
            if county == item.value:
                unique_counties[county]["number of tracts"] += 1
                pop = sheet.cell(row=item.row, column=4).value
                unique_counties[county]["population"] += pop

    # write results into a file
    result_file = open("censuspopdata_result.py", 'w')
    result_file.write(f"censuspopdata_result = {pprint.pformat(unique_counties)}")
    result_file.close()

    print("DONE.")


data_file = "censuspopdata_file.xlsx"
census_calc(data_file)

