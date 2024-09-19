#Moyo Fagbuyi, Margie Cao
# M & M
# SoftDev
# K06 -- 
# 2024-09-17
# time spent: 41 mins
import random

with open('occupations.csv','r') as text:
    data = text.readlines()
    #turnss file into a string  
    list = []
    data[0] = ""
    #removes the title lines
    for x in data :
        if not x  == "":
            str = x.split(",")
            list.append({str[0] : str[1][:-1]})
            #for every line
            #if the line has data,
            #make a dict with the job as key and % as value
            
    
    
'''

DISCO:

QCC:

- Is there a more efficent way to do the distrubition rahter than
having a list with 100 entries based on how common the job is?

HOW THIS SCRIPT WOKRS:


'''
print(list)