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

#progress towards completion nums
progress = [10, 20, 30, 40, 50, 60, 70, 80, 90]

#different types of goals and num of each required (these two work together)
activity = ["Class Presentation", "Career Day/Fair", "Career Cafe", "Career Panel", "Family Engagement", "Field Trip/Industry Tour", "Guest Speaker", "Meet the Professional", "Mock Interview"]
numRequired = [9, 1, 34, 4, 5, 4, 9, 4, 1]

#combine them into a dictionary
numForEachActivity = {}
n = 0
for i in activity:
    numForEachActivity[activity[n]] = numRequired[n]
    n = n + 1

#keep track of progress so far
numActual = {}
n = 0
for i in activity:
    numActual[activity[n]] = 0
    n = n + 1

#print(numActual)
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

#get the desired school
school = input("Which school's data would you like to view? (BHS, GHS, YHS, THS, YRA, QLMS, GMS, TMS, YMS)\n>")

n = 0
schools = []
for i in data:
    schools.append(data[n][2])
    n = n + 1

#grab the correct school   
if school in schools:
    subject = school
else:
    print("Invalid school entered, please try again.")

#track data completion
n = 0
for i in data:
    if subject == data[n][2]:
        print(data[n][1])
        numActual[data[n][1]] += 1
        n = n + 1
    else:
        print("not")
        n = n + 1

print(numActual)
def graph():
    plt.title(subject + " Progress Report")
    plt.xlabel("Activity")
    plt.ylabel("Progress (in percent)")
    plt.yticks([0, 25, 50, 75, 100])
    plt.bar(activity, progress)
    plt.show()

graph()