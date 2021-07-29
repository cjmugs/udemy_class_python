# Min for a FLask server to work 

from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello Chris!</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')