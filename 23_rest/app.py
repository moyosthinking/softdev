import urllib.request, json
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    key = 'https://api.nasa.gov/planetary/apod?api_key=dHGlhfwLl19MBXsLbGiguQeg30P7X7LJdOlEr4N7'
    data = urllib.request.urlopen(key)
    dictionary = json.loads(data.read())
    hdurl = dictionary.get('hdurl')
    description = dictionary.get('explanation')
    return render_template('main.html', photo=hdurl, description=description)

if __name__ == "__main__":
    app.debug = True
    app.run()
