# Margie Cao, Moyo Fagbuyi, Tim Ng
# System Level Programming
# SoftDev
# 2024-10-08
# 1.5 periods

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

import testmod0

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
 * Some will work as written;
 *  ...other sections will not. 

TASK:
 Predict which.
 1. Devise simple tests to isolate components/behaviors.
 2. Execute your tests.
 3. Process results.
 4. Findings yield new ideas for more tests? Yes: do them.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

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


@app.route("/auth", methods=['GET']) #, methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request) #returns link to current page
    print("***DIAG: request.args ***") 
    print(request.args) #returns agruments user inputtied, and sub1
    print("***DIAG: request.args['username']  ***")
    print(request.args['username']) #returns username sspecifally
    print("***DIAG: request.headers ***")
    print(request.headers) #gives like a bunch of information on the current website user
#     print("***DIAG: methods[0]***")
#     print(request.method)
    return testmod0.goo()  #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
