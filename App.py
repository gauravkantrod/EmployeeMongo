from flask import Flask
from flask_pymongo import PyMongo, MongoClient
from flask import jsonify, request
from bson.json_util import dumps
import json

from Employee import Employee

app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/employees"
#mongo = PyMongo(app)


client = MongoClient("mongodb://127.0.0.1:27017") #host uri
db = client.Employees #Select the database as Employees
employees = db.employees #Select the collection name as employees



@app.route('/')
@app.route('/index')
def app_check():
    return "Application is up and running."

@app.route("/get_all_data", methods = ['GET'])
def get_all_data():
    data_lst = []
    for d in  employees.find():
        data_lst.append(d)

    print(data_lst)

    return dumps(data_lst)

@app.route("/get_single_data", methods = ['GET'])
def get_data():
    return dumps(employees.find({'first_name':'Gaurav300'}))


@app.route('/insert_one', methods=['POST'])
def insert_one():

    data = request.json
    employees.insert_one(data)
    return "OK"

@app.route('/insert_many', methods=['POST'])
def insert_many():
    data = request.json
    employees.insert_many(data)

    return 'OK'




if __name__ == '__main__':
    app.run(debug=True)