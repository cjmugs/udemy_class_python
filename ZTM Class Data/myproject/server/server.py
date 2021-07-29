# Min for a FLask server to work 

from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/blog")
def blog():
    return "<p>THIS IS JUST A TEST SITE ABOUT BLOGS <br> FOR DEVELOPMENT MODE ONLY</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')