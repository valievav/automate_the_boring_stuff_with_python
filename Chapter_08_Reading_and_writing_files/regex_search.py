'''
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.
'''

import re, os


# extracting specific type of file
def find_files(extension, file_list):
    resulted_files = []
    for file in file_list:
        if file.endswith(f".{extension}"):
            resulted_files += [file]
    return resulted_files


# opening all txt files and searching for a match
def file_match_search(regex, files_list, path):
    for file in files_list:
        file_path = os.path.join(path, file)
        opened_file = open(file_path)
        lines = opened_file.readlines()
        opened_file.close()

        matches = []
        for line in lines:  # going through each line to detect one with the match
            if regex.search(line):
                matches.append(line)

        # printing results
        if matches:
            print(f"Found match in [{file}]:")
            for match in matches:
                print(" "*3 + f"{matches.index(match) + 1}. {match.strip()}")
        else:
            print(f"Found no match in [{file}]")


cwd = os.getcwd()
all_files = os.listdir(cwd)

# extracting available txt file names
extension = "txt"
txt_files = find_files(extension, all_files)
print(f"Available txt files in the working directory: ", end=" ")

for file in txt_files:
    print(f"{txt_files.index(file)+1}.", file, end=" ")

# getting user search regex
user_search = input(f"\nPlease enter regex for search:\n")

# finding lines with match
try:
    user_regex = re.compile(r"{0}".format(user_search))
    file_match_search(user_regex, txt_files, cwd)
except re.error:
    print("Entered regex with pattern error")

