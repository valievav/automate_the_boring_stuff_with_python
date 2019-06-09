'''
Created to practice csv data parsing from csv format into dictionary
'''

import csv

def data_reader(file):
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        capitals = dict(reader)
    return capitals