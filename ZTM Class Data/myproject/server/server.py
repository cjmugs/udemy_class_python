# Min for a FLask server to work 

from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/page2.html")
def page_2():
    return render_template('page2.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')