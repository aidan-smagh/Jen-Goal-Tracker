import csv
import matplotlib.pyplot as plt
import numpy as np
import sys

#command line arguments for dynamic file names
name = sys.argv[1]
#print(name)

#headers is a list of the first line in the csv file
headers = []

#data is a list containing other lists which are each line in the csv file
data = []

#read from the csv file
def read_csv(file_name):
    with open(name, mode = 'r') as file:
        csvFile = csv.reader(file)
        n = 0
        for lines in csvFile:
            if (n == 0):
                #print(lines)
                global headers
                headers = lines
                n = n + 1
            else:
                global data
                data.append(lines)
                n = n + 1

read_csv(name)
#print(headers)
#print(data)

n = 0
schools = []
for school in data:
    schools.append(data[n][2])
    n = n + 1

progress = 1

def dataForGraph():
    plt.title("Progress Report")
    plt.xlabel("Schools")
    plt.ylabel("Progress")
    plt.bar(schools, progress)
    plt.show()

dataForGraph()