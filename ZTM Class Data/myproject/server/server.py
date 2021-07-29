# Min for a FLask server to work 

from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return "<p>HELLO CHRIS, THIS IS JUST A TEST SITE <br> FOR DEVELOPMENT MODE ONLY</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')