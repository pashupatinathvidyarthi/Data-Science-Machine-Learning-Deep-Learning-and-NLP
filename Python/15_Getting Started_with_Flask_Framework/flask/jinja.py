## Building URL Dynamically
## Variable Rule
## Jinja 2 Template Engine


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
@app.route('/success/<score>')
def success(score):
    return "The marks you got is "+score

if __name__=="__main__":        ##This is entry of any .py file
    app.run(debug=True)   ## debuge=True means website getting update dynamically as we made chnage in the file


"""
To redirect to the paticular html file we need to create templates file inside 
flask and inside templates file html file name should be 'index.html' 
"""   