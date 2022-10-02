
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import json
from os import environ

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}
 
db = SQLAlchemy(app)
CORS(app)

class Staff(db.Model):
    __tablename__ = 'staff'
    # inventoryId = db.Column(db.Integer, primary_key=True)
    # storeName = db.Column(db.String(64), nullable=False)
    Staff_ID = db.Column(db.Integer, primary_key=True)
    Staff_FName = db.Column(db.String(64), nullable=False, unique=True)
    Staff_LName = db.Column(db.String(64), nullable=False, unique=True)
    Dept = db.Column(db.String(64), nullable=False, unique=True)
    Email = db.Column(db.String(64), nullable=False, unique=True)

    # staff_id = db.Column(db.String(64), nullable=False, primary_key=True)
    #price = db.Column(db.Float(precision=2), nullable=False)
    #stockCount = db.Column(db.Integer)
    # imageLink= db.Column(db.String(100), nullable=False)
    #userId = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(64), nullable=False, unique=True)
    

    def __init__(self, Staff_ID, Staff_FName, Staff_LName, Dept, Email):
        # self.inventoryId = inventoryId
        # self.storeName = storeName
        self.Staff_ID = Staff_ID
        self.Staff_FName = Staff_FName
        self.Staff_LName = Staff_LName
        self.Dept = Dept
        self.Email = Email
        # self.imageLink = imageLink
 
    def json(self):
        # "inventoryId": self.inventoryId,
        return {"staffID": self.Staff_ID, "Staff_FName": self.Staff_FName, "Staff_LName": self.Staff_LName, "Department": self.Dept, "Email": self.Email}

class Role(db.Model):
    __tablename__ = 'role'
    # inventoryId = db.Column(db.Integer, primary_key=True)
    # storeName = db.Column(db.String(64), nullable=False)
    Role_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(64), nullable=False, unique=True)
    description = db.Column(db.String(64), nullable=False, unique=True)


    # staff_id = db.Column(db.String(64), nullable=False, primary_key=True)
    #price = db.Column(db.Float(precision=2), nullable=False)
    #stockCount = db.Column(db.Integer)
    # imageLink= db.Column(db.String(100), nullable=False)
    #userId = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(64), nullable=False, unique=True)
    

    def __init__(self, Role_ID, Role_Name,description):
        # self.inventoryId = inventoryId
        # self.storeName = storeName
        self.Role_ID = Role_ID
        self.Role_Name = Role_Name
        self.description = description

        # self.imageLink = imageLink
 
    def json(self):
        # "inventoryId": self.inventoryId,
        return {"Role_ID": self.Role_ID, "Role_Name": self.Role_Name, "description": self.description} 


# show all inventory
@app.route("/staff")
def get_all_staff():
    staff_list = Staff.query.all()
    if len(staff_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "inventoryList": [staff.json() for staff in staff_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no staff"
        }
    ), 404

@app.route("/role")
def get_all_role():
    role_List = Role.query.all()
    if len(role_List):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "inventoryList": [role.json() for role in role_List]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no role"
        }
    ), 404

@app.route("/role/<string:Role_ID>/<string:Role_Name>/<string:description>", methods=['POST'])
def create_role(Role_ID,Role_Name,description):

    if (Role.query.filter_by(Role_ID=Role_ID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "Role_ID": Role_ID,
                    "Role_Name": Role_Name,
                    "Role_Name": description
                },
                "message": "Order already exists."
            }
        ), 400
 
    #data = request.get_json()
    #print("poopo" + data)
    new_role = Role(Role_ID, Role_Name,description)
 
    try:
        db.session.add(new_role)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "Role_ID": Role_ID,
                    "Role_Name": Role_Name,
                    "description": description,
                },
                "message": "An error occurred creating the order."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": new_role.json()
        }
    ), 201

@app.route('/role/delete/<string:Role_ID>',methods=['DELETE'])
def deleteInventory(Role_ID):
    role = Role.query.filter_by(Role_ID=Role_ID).first()
    if role:
            db.session.delete(role)
            db.session.commit()
            
            return jsonify(
                {
                    "code": 201,
                    "message": "Delete Successful."
                } ), 201

    else:
            return jsonify(
                {
                    "code": 404,
                    "message": "Delete unsuccessful as role does not exist."
                } ), 404

#update inventory by foodName
@app.route('/role/update/<string:Role_ID>/<string:Role_Name>/<string:description>',methods=['PUT'])
def updateInventory(Role_ID,Role_Name,description):
    role = Role.query.filter_by(Role_ID=Role_ID).first()

    if role:

        Role.query.filter_by(Role_ID=Role_ID).update(dict(Role_Name=Role_Name,description=description))

        db.session.commit()
        
        return jsonify(
            {
                "code": 201,
                "data": role.json(),
                "message": "Updated sucessfully"
            } ), 201
    
    return jsonify(
            {
                "code": 500,
                "data": {
                    "foodName": Role_Name
                },
                "message": "Inventory does not exist"
            }
        ), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
 

    