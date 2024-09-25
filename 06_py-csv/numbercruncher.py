# Moyo Fagbuyi, Margie Cao
# M & M
# SoftDev
# K06 -- Reading CSVs and storing them in dictionaries
# 2024-09-17
# time spent: 0.8

import random
import csv

'''

DISCO:

- Need to import csv module

QCC:

- Is there a more efficent way to do weighted distrubition rather than
having a list with 100 entries based on how common the job is?
- Possible to use ranges
- How could this script be generalized? Grabbing the header and
making it a variable instead of specifically making it look for the "Percentage" key

HOW THIS SCRIPT WORKS:

- We read the csv file with a dictionary reader that uses the headers as keys.
- We choose a random integer in the range of percentages possible
- We subtract from this integer the value of percentages until it hits a certain range (when it's under 0)
- We print out the job class value that represents the class for the specific range
- We break once it is found and the value is printed

'''

with open('occupations.csv','r') as text:
    data = csv.DictReader(text)
    #puts text into a list of dictionaries with heading as keys
    num = random.randint(0, 998)
    #random number for percentage
    for x in data:
        num = num - float(x["Percentage"])*10
        if num < 0:
            print(x["Job Class"])
            #when in range print job class value
            break;