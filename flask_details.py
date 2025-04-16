from flask import Flask
'''
It creates an instance of the flask class,
which will be your WSGI(Web server Gateway Interface) application.
'''

app=Flask(__name__)

@app.route("/")

def Welcome():
    return "hello world"

@app.route("/index")

def index():
    return "welcome in index"

if __name__=="__main__":
    app.run(debug=True)
