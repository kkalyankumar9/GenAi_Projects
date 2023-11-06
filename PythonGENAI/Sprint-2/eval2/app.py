from flask import Flask

app = Flask(__name__)
data={}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/create",methods=['GET', 'POST'])
def hello_world(data):
    username=input("Enter username")
    caption=input("Enter caption")
    data.append({"username":username,"caption":caption})
    return data
@app.route("/display_all",method=['GET'])
def post_viewing(data):
    return data
@app.route("/display_all/<id>",method=['DELETE'])
def post_viewing(data,id):
    for i in data:
        if i[_id]==id:
            return data

    