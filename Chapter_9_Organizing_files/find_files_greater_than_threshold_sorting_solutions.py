#! python3

# This module is created for files_greater_than_threshold_finder.py
# to be able to switch between different sorting solutions without changing the main code


# initial solution with separate list creation
def sort_results_through_new_list(files_list):
    """
    Sorts files list in desc order by the files size.\n
    This is done by creating a separate empty list and filling it in with max size values from the initial list.
    While sorted values are recorded into the new list, they are removed from the old list to save resources.
    :param files_list: list of lists
    :return: sorted files list, length of the sorted list
    """

    # list should not be empty to do the order
    if len(files_list) == 0:
        return

    # creating new list with ordered results
    sorted_files_list = []

    while True:
        if len(files_list) > 1:  # list must me over 1 sub-list to sort it
            max_size = 0
            max_size_index = 0

            for i in range(len(files_list)):  # going through each sub-list
                if files_list[i][1] > max_size:  # evaluating each [1] value
                    max_size = files_list[i][1]  # finding max size in a current list
                    max_size_index = i

            sorted_files_list.append(files_list[max_size_index])  # recording max size sub-list in a new list after iterating through whole old list length
            del files_list[max_size_index]  # removing max value sub-list from the old list

        else:
            sorted_files_list.append(files_list[0])  # adding last sub-list to the new list
            del files_list[0]  # removing last sub-list from the old list
            list_length = len(sorted_files_list)
            return sorted_files_list, list_length


# more advance solution with lambda usage
def sort_results_with_lambda(files_list):
    """
    Sorts files list in desc order by the files size.
    :param files_list: list of lists
    :return: sorted files list, length of the sorted list
    """

    sorted_results = sorted(files_list, key=lambda x: x[1], reverse=True)
    list_length = len(sorted_results)
    return sorted_results, list_length


# method to switch between solutions by commenting out non-required method
def sort_results_by_size(files_to_sort):
    return sort_results_through_new_list(files_to_sort)
    # return sort_results_with_lambda(files_to_sort)


if __name__ == "__main__":

    files_to_sort = [["first", 40], ["second", 60], ["third", 1], ["forth", 200]]
    x = sort_results_by_size(files_to_sort)
    print(x)


