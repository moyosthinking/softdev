# Margie Cao, Moyo Fagbuyi, Tim Ng
# System Level Programming
# SoftDev
# 2024-10-09
# o 

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request  

import rev

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/",  methods=['GET'])  #, (methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request) # prints out home route to terminal
    print("***DIAG: request.args ***")
    print(request.args) # this is ImmutableMultiDict([])
#     print("***DIAG: request.args['username']  ***") 
#     print(request.args['username']) #this kinda breaks everything
    print("***DIAG: request.headers ***")
    print(request.headers) #gives like a bunch of information on the current website user
#     print("***DIAG: methods[0]***")
#     print(request.method)
    return render_template( 'login.html' )

inputted = []

@app.route("/auth", methods=['GET']) #, methods=['GET', 'POST'])
def post():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request) #returns link to current page
    print("***DIAG: request.args ***") 
    inputted = request.args
    print(inputted) #returns agruments user inputtied, and sub1
    print("***DIAG: request.args['username']  ***")
    print(request.args['username']) #returns username sspecifally
    print("***DIAG: request.headers ***")
    print(request.headers) #gives like a bunch of information on the current website user
#     print("***DIAG: methods[0]***")
#     print(request.method)
    return render_template('response.html', inputted=inputted)



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
