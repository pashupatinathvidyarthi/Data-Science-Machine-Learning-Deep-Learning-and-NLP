from flask import Flask

"""
It creates an instances of the Flask class,
which will be your WSGI(Web Server Gateway Interface) application.
"""
##WSGI Application
app=Flask(__name__)

@app.route("/") ## / means home page of web page
def welcome():
    return "Welcome to this Falsk.This should be amazing course"

if __name__=="__main__":        ##This is entry of any .py file
    app.run(debug=True)     