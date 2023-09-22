from flask import Flask
from pymongo import MongoClient
from flask.json import jsonify

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
mydatabase = client.jeeva
mycollection = mydatabase.users

@app.route("/",methods=(["GET"]))
def home():
    users_list = []
    for i in mycollection.find():
        user = {
            "name": i['name'],
            "password":i['password']
        }
        users_list.append(user)

    return jsonify(users_list)

@app.route("/register",methods=(["GET","POST"]))
def register():

    new_user = {
        "name":"priya",
        "password":"priyacute"
    }

    mydatabase.users.insert_one(new_user)

    return "data successfully inserted"

@app.route("/login",methods=(["GET"]))
def login():
    login_user = []

    for i in mycollection.find({"name":"priyanka"}):
        login_user.append(i['name'])

    if login_user:
        return "you have account"
    else:
        return "you have no account"


@app.route("/update")
def update():
    mycollection.update_one({"name":"priya"})

app.run(debug=True)