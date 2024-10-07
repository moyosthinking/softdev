'''
Moyo Fagbuyi, Sascha Gordon-Zolov, Ziyad Hamed (PPAP)
SoftDev
K09 -- Softserve -- Using the random occupation from csv file and returning it through the use of the Flask import.
2024-09-20
time spent: 2 hours
'''

from flask import Flask, render_template # imports the flask command
import csv
import random

with open('data/occupations.csv', newline='') as csvfile: # reads the csv file using python's csv import
    occupations = csv.reader(csvfile)
    dic = {} # initatizes a new dictionary
    for row in occupations:
        if (row[0] != 'Job Class') and (row[0] != 'Total'): # removes the first and last keys
            dic.update({row[0]: [float(row[1]), row[2]]}) # updates the dictionary with the occupations as keys and the percentage as values.

def randomSelection(): # function for choosing a random number with a weighted percentage
    finalText = "" # creates the starting string
    for key in dic.keys(): # appends each key in the list of keys into the finalText string to return as one big string
        finalText = finalText # uses the <br> command which is commonly seen in html which is similar to \n
    x = random.uniform(0.0,99.8)
    for key, value in dic.items():
        x = x - value[0] # each key has a range and this subtracts until it is chosen
        if x <= 0:
            return finalText + "Selected Occupation: " + key# adds the randaomly selected occupation html
        
        
app = Flask(__name__) # initalizes the flask application
@app.route("/wdywtbwygp") # routes using the '/' directory
    
def occ_template():
    return render_template("tablified.html", title = "Occupation Title Combined", occupations = dic.items(), rand = randomSelection())

app.run()