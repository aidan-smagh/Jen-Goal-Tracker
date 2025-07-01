import csv
import matplotlib.pyplot as plt
import numpy as np
import sys

#command line arguments for dynamic file names
name = sys.argv[1]
#print(name)

def read_csv(file_name):
    with open(name, mode = 'r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)

read_csv(name)