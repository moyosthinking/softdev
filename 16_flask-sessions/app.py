# Margie Cao, Moyo Fagbuyi, Tim Ng
# System Level Programming
# SoftDev
# 2024-10-09
# o

from flask import Flask, render_template, request, session #this one stores like verything
import os
from utl import ants


app = Flask(__name__)

@app.route("/",  methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' ) #renders homepage


@app.route("/auth", methods=['GET', 'POST'])
def post():
    session[ants.poop()] = request.args['username']
#     return render_template('response.html', inputted=inputted)
    return "poop"



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()