import flask
from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if (__name__ == '__main__'):
    app.run(debug=False, host="66.11.118.34", port="80")