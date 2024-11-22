import urllib.request, json
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    key = 'http://www.omdbapi.com/?i=tt3896198&apikey=b113e02'
    data = urllib.request.urlopen(key)
    dictionary = json.loads(data.read())
    hdurl = dictionary.get('Title')
    description = dictionary.get('explanation')
    return render_template('main.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
