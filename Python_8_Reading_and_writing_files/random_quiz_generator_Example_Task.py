#! python3
# random_quiz_generator_Example_Task.py - Creates quizzes with questions and answers in random order, along with the answer key.

import os, random
from random_quiz_csv_data_reader import data_reader
from random_quiz_csv_data_writer import data_writer

# writing-reading csv data is done for practicing purposes
data_writer("random_quiz_data.csv")# populating csv file with quiz data
quiz_data = data_reader("random_quiz_data.csv") # getting data from csv as a dictionary

# creating work folder
working_dir = "C:\\Users\\Venus\\Downloads\\US State Capitals Quiz"
os.makedirs(working_dir, exist_ok=True) # if path already exists, no errors raised
os.chdir(working_dir)

number_of_files = 35

def files_generator(quiz_data, number_of_files):

    # generating quiz files
    for quiz_number in range(number_of_files):

        file_questions = open(f"US_State_Capitals_Quiz_{quiz_number+1}.txt", "w")
        file_questions.write("Date:\n"
                             "Student:\n\n" +
                             " "*5 + f"US State Capitals QUIZ (Form {quiz_number+1})\n"
                             "\n" )
    
        file_answers = open(f"US_State_Capitals_Quiz_{quiz_number+1}_Answers.txt", "w")
        file_answers.write(f"US State Capitals QUIZ answers (Form {quiz_number-1})\n\n")


        states_list = list(quiz_data.keys()) # generating list of states to iterate through
        random.shuffle(states_list) # to generate different states order questions for each file
        question_number = 0

        # generating questions and answers
        for state in states_list:
            question_number += 1
            file_questions.write(f"\n{question_number}. What is a capital of {state}?\n")

            correct_answer = quiz_data[state]
            capitals_list = list(quiz_data.values()) # generating new list on each iteration because of removing the correct answer
            capitals_list.remove(correct_answer)
            wrong_answers = random.sample(capitals_list, 3)
            answers = [correct_answer] + wrong_answers
            random.shuffle(answers)

            abcd = ["A", "B", "C", "D"]
            for i in range(4):
                file_questions.write(f"{abcd[i]}. {answers[i]}\n")
            file_answers.write(f"{question_number}. {abcd[answers.index(correct_answer)]}. {correct_answer}\n")

        file_answers.close()
        file_questions.close()

files_generator(quiz_data, number_of_files)
