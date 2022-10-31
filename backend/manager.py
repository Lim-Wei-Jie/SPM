
import os
from unittest import skip
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import json
from os import environ

#new
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}
 
db = SQLAlchemy(app)
CORS(app)

class Staff(db.Model):
    __tablename__ = 'staff'
    Staff_ID = db.Column(db.String(64), primary_key=True)
    Staff_FName = db.Column(db.String(64), nullable=False, unique=True)
    Staff_LName = db.Column(db.String(64), nullable=False, unique=True)
    Dept = db.Column(db.String(64), nullable=False, unique=True)
    Email = db.Column(db.String(64), nullable=False, unique=True)
    System_Role = db.Column(db.Integer, primary_key=True)
    

    def __init__(self, Staff_ID, Staff_FName, Staff_LName, Dept, Email, System_Role):
        self.Staff_ID = Staff_ID
        self.Staff_FName = Staff_FName
        self.Staff_LName = Staff_LName
        self.Dept = Dept
        self.Email = Email
        self.System_Role = System_Role
 
    def json(self):
        return {"staffID": self.Staff_ID, "Staff_FName": self.Staff_FName, "Staff_LName": self.Staff_LName, "Department": self.Dept, "Email": self.Email, "System Role": self.System_Role}

class Role(db.Model):
    __tablename__ = 'role'
    Role_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(64), nullable=False, unique=True)
    Role_Desc = db.Column(db.String(512), nullable=False, unique=True)
    Date_Created = db.Column(db.String(64), nullable=False, unique=True, default=datetime.utcnow)
    

    def __init__(self, Role_ID, Role_Name,Role_Desc,Date_Created=datetime.now()):
        self.Role_ID = Role_ID
        self.Role_Name = Role_Name
        self.Role_Desc = Role_Desc
        self.Date_Created = Date_Created
 
    def json(self):
        #return {"Role_ID": self.Role_ID, "Role_Name": self.Role_Name, "Role_Desc": self.Role_Desc, "Date_Created": self.Date_Created} 
        return {"Role_ID": self.Role_ID, "Role_Name": self.Role_Name, "Role_Desc": self.Role_Desc} 


class Course(db.Model):
    __tablename__ = 'course'
    Course_ID = db.Column(db.Integer, primary_key=True)
    Course_Name = db.Column(db.String(64), nullable=False, unique=True)
    Course_Desc = db.Column(db.String(512), nullable=False, unique=True)
    Course_Status = db.Column(db.String(64), nullable=False, unique=True)
    Course_Type = db.Column(db.String(64), nullable=False, unique=True)
    Course_Category = db.Column(db.String(64), nullable=False, unique=True)
    

    def __init__(self, Course_ID, Course_Name,Course_Desc,Course_Status,Course_Type,Course_Category):
        self.Course_ID = Course_ID
        self.Course_Name = Course_Name
        self.Course_Desc = Course_Desc
        self.Course_Status = Course_Status
        self.Course_Type = Course_Type
        self.Course_Category = Course_Category
 
    def json(self):
        return {"Course_ID": self.Course_ID, "Course_Name": self.Course_Name, "Course_Desc": self.Course_Desc, "Course_Status": self.Course_Status, "Course_Type":self.Course_Type, "Course_Category":self.Course_Category} 

class Skill(db.Model):
    __tablename__ = 'Skill'
    Skill_ID = db.Column(db.Integer, primary_key=True)
    Skill_Name = db.Column(db.String(64), nullable=False)
    Skill_Desc = db.Column(db.String(255), nullable=False)
    Date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def json(self):

        return {"Skill_ID": self.Skill_ID , "Skill_Name": self.Skill_Name, "Skill_Desc": self.Skill_Desc , "Date_created": self.Date_created}
    
    def __init__(self, Skill_ID, Skill_Name, Skill_Desc, Date_created=None):
        self.Skill_ID = Skill_ID 
        self.Skill_Name = Skill_Name
        self.Skill_Desc = Skill_Desc
        if Date_created is None:
            self.Date_created = datetime.utcnow()
        else:
            self.Date_created = Date_created

class Skill_Assign(db.Model):
    __tablename__ = 'Skill_Assignment'
    Course_ID = db.Column(db.String(64), nullable=False, primary_key=True)
    Skill_ID = db.Column(db.Integer, nullable=False, primary_key=True)

    def __init__(self, Skill_ID,Course_ID):
        self.Skill_ID = Skill_ID
        self.Course_ID = Course_ID
 
    def json(self):
        return { "Skill_ID": self.Skill_ID,"Course_ID": self.Course_ID } 

class Role_Assign(db.Model):
    __tablename__ = 'Role_Assignment'
    Role_ID = db.Column(db.Integer, nullable=False, primary_key=True)
    Skill_ID = db.Column(db.Integer, nullable=False, primary_key=True)

    def __init__(self, Role_ID,Skill_ID):
        self.Role_ID = Role_ID
        self.Skill_ID = Skill_ID
 
    def json(self):
        return { "Role_ID": self.Role_ID, "Skill_ID": self.Skill_ID} 

# show all inventory
@app.route("/staff")
def get_all_staff():
    staff_list = Staff.query.all()
    print(staff_list)
    if len(staff_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staffList": [staff.json() for staff in staff_list]
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
                    "Role": [role.json() for role in role_List]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no role"
        }
    ), 404

@app.route("/role/create/<string:Role_ID>/<string:Role_Name>/<string:Role_Desc>", methods=['GET','POST'])
def create_role(Role_ID,Role_Name,Role_Desc):

    if (Role.query.filter_by(Role_ID=Role_ID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "Role_ID": Role_ID,
                    "Role_Name": Role_Name,
                    "Role_Desc": Role_Desc
                },
                "message": "Role already exists."
            }
        ), 400
    new_role = Role(Role_ID, Role_Name,Role_Desc,datetime.utcnow())
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
                    "Role_Desc": Role_Desc,
                },
                "message": "An error occurred creating the Role."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": new_role.json()
        }
    ), 201

@app.route('/role/delete/<string:Role_ID>',methods=['DELETE'])
def delete_role(Role_ID):
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

#update role by ID
@app.route('/role/update/<string:Role_ID>/<string:Role_Name>/<string:Role_Desc>',methods=['PUT'])
def updateRole(Role_ID,Role_Name,Role_Desc):
    role = Role.query.filter_by(Role_ID=Role_ID).first()

    if role:

        Role.query.filter_by(Role_ID=Role_ID).update(dict(Role_Name=Role_Name,description=Role_Desc))

        db.session.commit()
        
        return jsonify(
            {
                "code": 201,
                "data": role.json(),
                "message": "Role Updated sucessfully"
            } ), 201
    
    return jsonify(
            {
                "code": 500,
                "data": {
                    "foodName": Role_Name
                },
                "message": "Role does not exist"
            }
        ), 500

#get role from id
@app.route("/role/<string:Role_ID>",methods=['GET'])
def get_role_id(Role_ID):
    role = Role.query.filter_by(Role_ID=Role_ID).first()
    print(role)
    if role:
        return jsonify(
            {
                "code": 200,
                "data": {
                        "Role": [role.json()]
                }            
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no such role"
        }
    ), 404

#get role from name
@app.route("/role/name/<string:role_Name>",methods=['GET'])
def get_role_name(role_Name):
    #role_List = Role.query.filter(Role.Role_Name.like(Role_Name)).all()
    role_List = Role.query.filter(Role.Role_Name.like(f'%{role_Name}%')).all()
    print(role_List)
    if role_List:
        return jsonify(
            {
                "code": 200,
                "data": {
                        "Role": [role.json() for role in role_List]
                }            
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no such role"
        }
    ), 404

#viewing the role_assignment table
@app.route("/role/getskill")
def get_mapped_skill_to_role():
    #list
    Skill_Role_Map = Role_Assign.query.all()
    if len(Skill_Role_Map):
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    
                    #turn python data into javascript object
                    "maps": [Skill_Assign.json() for Skill_Assign in Skill_Role_Map]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Skills assigned to Roles."
        } 
    ), 404

#get skills from role_ID
@app.route("/role/getskill/<string:Role_ID>",methods=['GET'])
def get_skill_list_by_Role(Role_ID):
    list_ofID = get_skill_id_by_role(Role_ID) 
    #check list of ID ##Need to add a validator here to check if it returns a list or error
    print(list_ofID)
    if list_ofID:
        filtered_list = filter_skillID(list_ofID)
        skill_list = Skill.query.filter(Skill.Skill_ID.in_(filtered_list)).all()
        if skill_list:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                            "Skill": [skill.json() for skill in skill_list]
                    }            
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There is no such skill"
            }
        ), 404
    return jsonify(
    {
        "code": 404,
        "message": "There is no such skill"
    }), 404     
#filter only skillID
def filter_skillID(list_of_id):
    list_onlyID = []
    for data in list_of_id:
        #print(data.Skill_ID)
        list_onlyID.append(str(getattr(data,"Skill_ID")))
    return list_onlyID
#get skill from associative table using role_id
def get_skill_id_by_role(Role_ID):
    role_list = Role_Assign.query.filter_by(Role_ID=Role_ID).all()
    if role_list:
        return role_list

#mapping skills to role
@app.route("/role/roleassignskills/<string:Role_ID>/<string:Skill_ID>", methods=['GET','POST'])
def role_to_skill_assignment(Role_ID,Skill_ID):
    Skill_ID = Skill_ID.replace("[","")
    Skill_ID = Skill_ID.replace("]","")
    skill_arr = Skill_ID.split(",")
    if_duplicate_err = ""

    for skill in skill_arr:
        print(skill)
        if (Role_Assign.query.filter(Role_Assign.Role_ID.like(Role_ID),Role_Assign.Skill_ID.like(skill)).first()):
            if_duplicate_err += str(skill)
        
        new_role_assignment = Role_Assign(Role_ID,skill)
        try:
            db.session.add(new_role_assignment)
            db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,
                    "data": {

                        "Role_ID": Role_ID,
                        "Skill_ID": skill
                        
                    },
                    "message": "An error occurred when assigning the skill to role."
                }
            ), 500
    return jsonify(
        {
            "code": 201,
            "data": new_role_assignment.json()
        }
    ), 201 

#delete skills from role
@app.route("/role/roledeleteskills/<string:Role_ID>/<string:Skill_ID>", methods=['GET','POST'])
def role_to_skill_delete(Role_ID,Skill_ID):
    
    Skill_ID = Skill_ID.replace("[","")
    Skill_ID = Skill_ID.replace("]","")
    skill_arr = Skill_ID.split(",")

    for skill in skill_arr:
        print(skill)
        role_skill_assignment = Role_Assign.query.filter(Role_Assign.Role_ID.like(Role_ID),Role_Assign.Skill_ID.like(skill)).first()
        if role_skill_assignment:
                db.session.delete(role_skill_assignment)
                db.session.commit()
        else:
            return jsonify(
                {
                    "code": 404,
                    "message": "Delete unsuccessful as role does not exist."
                } ), 404
    return jsonify(
        {
            "code": 201,
            "data": str(skill_arr)
        }
    ), 201 





#for skill-course assignment
@app.route("/skill")
def get_all_skill():
    #list
    Skilllist = Skill.query.all()
    if len(Skilllist):
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    
                    #turn python data into javascript object
                    "books": [Skill.json() for Skill in Skilllist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Skills."
        }
    ), 404
    



@app.route("/skill/<string:Skill_ID>/<string:Skill_Name>/<string:Skill_Desc>/<string:Date_created>", methods=['GET','POST'])
def create_skill(Skill_ID,Skill_Name,Skill_Desc,Date_created):

    if (Skill.query.filter_by(Skill_ID = Skill_ID ).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "Skill_ID": Skill_ID,
                    "Skill_Name": Skill_Name,
                    "Skill_Name": Skill_Desc,
                    "Date_created":Date_created
                },
                "message": "Skill already exists."
            }
        ), 400
 
    #data = request.get_json()
    #print("poopo" + data)
    new_skill = Skill(Skill_ID,Skill_Name,Skill_Desc,Date_created)
 
    try:
        db.session.add(new_skill)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "Skill_ID": Skill_ID,
                    "Skill_Name": Skill_Name,
                    "Skill_Name": Skill_Desc,
                    "Date_created":Date_created
                },
                "message": "An error occurred creating the Skill."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": new_skill.json()
        }
    ), 201 
    
#get courses from skill_ID
@app.route("/skill/getcourse/<string:Skill_ID>",methods=['GET'])
def get_course_list_by_Skill(Skill_ID):
    list_ofID = get_course_id_by_skill(Skill_ID)
    if list_ofID:
        filtered_list = filterID(list_ofID)
        course_list = Course.query.filter(Course.Course_ID.in_(filtered_list)).all()
        if course_list:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                            "Course": [course.json() for course in course_list]
                    }            
                }
            )
    return jsonify(
        {
            "code": 404,
            "message": "There is no course"
        }
    ), 404



#filter only courseID
def filterID(list_of_id):
    list_onlyID = []
    for data in list_of_id:
        list_onlyID.append(str(getattr(data,"Course_ID")))
    return list_onlyID

#get course from associative table using skill_id
def get_course_id_by_skill(Skill_ID):
    skill_list = Skill_Assign.query.filter_by(Skill_ID=Skill_ID).all()
    if skill_list:
        return skill_list    

#viewing the skill_assignment table
@app.route("/skill_course_assignment")
def get_mapped_skill_to_course():
    #list
    Skill_Course_Map = Skill_Assign.query.all()
    if len(Skill_Course_Map):
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    
                    #turn python data into javascript object
                    "maps": [Skill_Assign.json() for Skill_Assign in Skill_Course_Map]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Skills assigned to Courses."
        }
    ), 404


@app.route("/skill/<string:Skill_ID>/<string:Course_ID>/", methods=['GET','POST'])
def skill_to_course_assignment(Skill_ID,Course_ID):

    if (Skill_Assign.query.filter_by(Skill_ID = Skill_ID ,Course_ID=Course_ID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    
                    "Skill_ID": Skill_ID,
                    "Course_ID": Course_ID
                    
                },
                "message": "Skill-course already exists."
            }
        ), 400
    new_skill_assignment = Skill_Assign(Course_ID,Skill_ID)
 
    try:
        db.session.add(new_skill_assignment)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    
                    "Skill_ID": Skill_ID,
                    "Course_ID": Course_ID
                },
                "message": "An error occurred when assigning the skill to course."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": new_skill_assignment.json()
        }
    ), 201 



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)







    