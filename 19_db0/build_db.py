#Margie Cao, Moyo Fagbuyi, Tim Ng
#SoftDev
#SLP
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events, lets us execute statements and fetech results from db

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

command = "CREATE TABLE student(name TEXT, id INTEGER PRIMARY KEY)"          # test SQL stmt in sqlite3 shell, save as string

names = []
idd = []
with open('students.csv','r') as text:
    data = csv.DictReader(text)

    for row in data:
        names.append(row.get("name")) #puts all names into a list
        idd.append(int(row.get("id")))
        
#print(info)

for pers in info:
    command += "\n INSERT INTO student VALUES "  
    
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
