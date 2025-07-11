import csv
import matplotlib.pyplot as plt
import numpy as np
import sys

#command line arguments for dynamic file names
name = sys.argv[1]

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

#read from the csv file
def read_csv(file_name):
    with open(name, mode = 'r') as file:
        csvFile = csv.reader(file)
        n = 0
        for lines in csvFile:
            if (n == 0):
                global headers
                headers = lines
                n = n + 1
            else:
                global data
                data.append(lines)
                n = n + 1

read_csv(name)

#get the desired school
school = input("Which school's data would you like to view? (BHS, GHS, YHS, THS, YRA, QLMS, GMS, TMS, YMS)\n>")

#gets a list of all schools in the provided csv file
n = 0
schools = ["BHS", "GHS", "YHS", "THS", "YRA", "QLMS", "GMS", "TMS", "YMS"]
#for i in data:
#    n = n + 1

#grab the correct school   
if school in schools:
    subject = school
else:
    print("Invalid school entered, please try again.")

#track data completion
n = 0
for i in data:
    if subject == data[n][2]:
        numActual[data[n][1]] += 1
        n = n + 1
    else:
        n = n + 1

#reads from the dictionary and gets the percentage towards completion value
def getProgressNums():
    realProgress = []
    for key in numActual.keys():
        realProgress.append(numActual[key])
    n = 0
    finalProgress = []
    for i in realProgress:
        finalProgress.append(realProgress[n] / numRequired[n])
        n = n + 1

    return finalProgress 

#constructs the bar graph
def graph():
    plt.figure(figsize = (14, 6))
    plt.title(subject + " Progress Report")
    plt.xlabel("Activity")
    plt.ylabel("Progress")
    plt.ylim(0, 1.0)
    plt.yticks(np.arange(0, 1.25, 0.25))
    plt.bar(activity, getProgressNums())
    plt.show()

graph()