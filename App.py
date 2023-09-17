from flask import Flask
from flask import render_template

App = Flask(__name__)

@App.route('/')
def login():
    return render_template('index.html')

if __name__ == '__main__':
    App.run(debug=True)