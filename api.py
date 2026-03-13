### Put and Delete
### Working with API's --- json


from flask import Flask, jsonify, request

app=Flask(__name__)
 
##Initial Data in my to do List
items={
    {"id":1, "name":"Item 1", "description":"This is item 1"},
    {"id":2, "name":"Item 2", "description":"This is item 2"}
}

@app.route('/')
def home():
    return "Welcome To The Sample To Do List App"


## Get : Retrieve all the items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)


if __name__ == '__main__':
    app.run(debug=True)