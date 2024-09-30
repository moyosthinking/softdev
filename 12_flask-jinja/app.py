# Placeholder x 3
# Moyo, Will, Daniel
# SoftDev
# Sep 2024

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
<your response here>

Q1:
<your response here>

Q2:
<your response here>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
# (log prediction before executing...)
# A0: you'll get a 404 error
#~~~~~~~~~~~~~~~~~~~~~~~~~n a new directory in your workshop, save a copy of the starter kit for using flask (and its Jinja2 templating engine) to serve templated pages.
#As a team...~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Moyo Fagbuyi"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: Can all of your teammates confidently predict the URL to use to load this page?
# A1: thought it was http://127.0.0.1:5000/templates/model_tmplt.html byt that doesnt seem to work
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    # A2:    first is the end of the web link, which page, secomd like a tag, and third is a lsit for something
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()
