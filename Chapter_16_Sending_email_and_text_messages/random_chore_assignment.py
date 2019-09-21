'''
Write a program that takes a list of people’s email addresses and a list
of chores that need to be done and randomly assigns chores to people.
Email each person their assigned chores.
'''
import os, openpyxl, random

def random_tasks_assignment(cwd, file_name, emails_sheet, tasks_sheet, tasks_per_person, assigned_tasks_sheet):

    # verify that path exists
    if not os.path.isdir(cwd):
        print(f'Path "{cwd}" does not exists.\nExiting the program.')
        return

    os.chdir(cwd)

    # verify that file exists
    if file_name not in os.listdir(cwd):
        print(f"File '{file_name}' does not exist in path {cwd}.\nExiting program.")
        return

    wb = openpyxl.load_workbook(file_name)

    # verify that data sheets exist
    if emails_sheet not in wb.sheetnames or tasks_sheet not in wb.sheetnames:
        print(f"File doesn't have sheet with name '{emails_sheet}' or '{tasks_sheet}'.\nExiting program.")

    # extract emails into variable
    sheet = wb[emails_sheet]
    emails = []
    for cell in sheet['A']:
        emails.append(cell.value)

    # extract tasks into variable
    sheet = wb[tasks_sheet]
    tasks = []
    for cell in sheet['A']:
        tasks.append(cell.value)

    # verify all tasks can be assigned
    if tasks_per_person*len(emails) != len(tasks):
        print(f"Not all tasks can be matched. Please enter correct tasks per person value, "
              f"update emails number or tasks number.\nExiting program.")
        return

    # assign tasks
    assigned_tasks = {}
    for email in emails:
        random_assignment = random.randint(0, len(tasks)-1)
        assigned_tasks.setdefault(email, tasks[random_assignment])
        del tasks[random_assignment]

    # connect to email server





active_directory = r"D:\Practice Python"
file = "randon_chore_assignment_file.xlsx"
emails_sheet_list = "Emails"
tasks_sheet_list = "Tasks"
tasks_per_person = 1
result_sheet = "Assigned_tasks"

random_tasks_assignment(active_directory, file, emails_sheet_list, tasks_sheet_list, tasks_per_person, result_sheet)

