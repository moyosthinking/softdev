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

c.execute(command)

names = []
idd = []
with open('students.csv','r') as text:
    data = csv.DictReader(text)

    for row in data:
        names.append(row.get("name")) #puts all names into a list
        idd.append(int(row.get("id")))

x = 0
for pers in names:
    c.execute(f'INSERT student (name, id) VALUES ("{pers}", {idd[x]})')
    x += 1

coursesDB = "CREATE TABLE course(code TEXT, mark INTEGER, id INTEGER)"   # no primary key bc we can have repateint grades and ids
course = []
mark = []
idCourse = []

with open('courses.csv','r') as text:
    data = csv.DictReader(text)

    for row in data:
        course.append(row.get("code")) #puts all names into a list
        mark.append(int(row.get("mark")))
        idCourse.append(int(row.get("id")))

#print(course)
#print(mark)
#print(idCourse)

c.execute(coursesDB)

y = 0
for classs in course:
    c.execute(f'INSERT course(code, mark, id) VALUES ("{classs}", {mark[y]}, {idCourse[y]})')
    y += 1


#==========================================================

db.commit() #save changes
db.close()  #close database
