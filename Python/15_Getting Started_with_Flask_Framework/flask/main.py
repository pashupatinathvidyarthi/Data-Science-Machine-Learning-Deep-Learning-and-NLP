from flask import Flask,render_template 

"""
It creates an instances of the Flask class,
which will be your WSGI(Web Server Gateway Interface) application.
"""
##WSGI Application
app=Flask(__name__)

@app.route("/") ## / means home page of web page
def welcome():
    return "<html><h1>Welcome to the Flask</h1></html"

@app.route("/index")
def index():
    return render_template('index.html')

if __name__=="__main__":        ##This is entry of any .py file
    app.run(debug=True)   ## debuge=True means website getting update dynamically as we made chnage in the file   