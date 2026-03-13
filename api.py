### Put and Delete
### Working with API's --- json


from flask import Flask, jsonify, request

app=Flask(__name__)
 
##Initial Data in my to do List
items={
    {"id":1, "name":"Item 1", "description":"This is item 1"},
    {"id":2, "name":"Item 2", "description":"This is item 2"}
}


if __name__ == '__main__':
    app.run(debug=True)