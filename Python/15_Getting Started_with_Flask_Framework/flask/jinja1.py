## Building URL Dynamically
## Variable Rule
## Jinja 2 Template Engine


## Jinja 2 Tmplate Engine
"""
Method 01
{{  }} expressions to print output in html

Method 2
{%...%} conditions, for loops,while loop

Method 3
{#...#} this is for comment
"""

from flask import Flask,render_template,request

"""
It creates an instances of the Flask class,
which will be your WSGI(Web Server Gateway Interface) application.
"""
##WSGI Application
app=Flask(__name__)

@app.route("/") ## / means home page of web page
def welcome():
    return "<html><h1>Welcome to the Flask</h1></html"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

## Varibale Rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('result.html',results=res)


## Varibale Rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res=" PASSED"
    else:
        res=" FAILED"
    
    exp={'Score':score,"Result":res}
    return render_template('result1.html',results=exp)



if __name__=="__main__":      
    app.run(debug=True)   