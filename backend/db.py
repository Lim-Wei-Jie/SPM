from tkinter import CASCADE
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from sqlalchemy.orm import relationship,backref
from sqlalchemy import MetaData
#from skill_assign import skill_assignment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)



            
class Registration(db.Model):
    __tablename__ = 'registration'

    Reg_ID = db.Column(db.Integer, primary_key=True)
    Course_ID = db.Column(db.String(64), nullable=False)
    Staff_ID = db.Column(db.String(255), nullable=False)
    Reg_Status = db.Column(db.String(64), nullable=False)
    Completion_Status = db.Column(db.String(64), nullable=False)
  

    def json(self):
        return {"Reg_ID": self.Reg_ID, "Course_ID": self.Course_ID , "Staff_ID": self.Staff_ID, "Reg_Status": self.Reg_Status, "Completion_Status":self.Completion_Status}
    
    
    def __init__(self, Reg_ID, Course_ID, Staff_ID, Reg_Status,Completion_Status):
        self.Reg_ID = Reg_ID 
        self.Course_ID = Course_ID
        self.Staff_ID = Staff_ID
        self.Reg_Status = Reg_Status
        self.Completion_Status = Completion_Status
    
    

class LJPS_Assignment(db.Model):
    __tablename__ = 'LJPS_Assignment'


    LJPS_ID = db.Column(db.String(255), nullable=False, primary_key=True)
    Staff_ID = db.Column(db.String(255), nullable=False, primary_key=True)
    Role_ID = db.Column(db.String(255), nullable=False, primary_key=True)

    def __init__(self,  LJPS_ID ,Staff_ID ,Role_ID):
        
        
        self.LJPS_ID = LJPS_ID
        self.Staff_ID = Staff_ID
        self.Role_ID = Role_ID
 
    def json(self):
        return { "LJPS_ID": self.LJPS_ID,"Staff_ID": self.Staff_ID, "Role_ID":self.Role_ID} 
    
    


class LJPS_Course_Assignment(db.Model):
    __tablename__ = 'LJPS_Course_Assignment'


    LJPS_ID = db.Column(db.String(255), nullable=False, primary_key=True)
    Course_ID = db.Column(db.String(64), nullable=False, primary_key=True)


    def __init__(self,  LJPS_ID ,Course_ID):
        
        
        self.LJPS_ID = LJPS_ID
        self.Course_ID = Course_ID
 
    def json(self):
        return { "LJPS_ID": self.LJPS_ID,"Course_ID": self.Course_ID} 
    
    


    
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
    Role_ID = db.Column( db.String(255), nullable=False, primary_key=True, unique=True)
    Role_Name = db.Column(db.String(64), nullable=False)
    Role_Desc = db.Column(db.String(512), nullable=False)
    Date_Created = db.Column(db.String(64), nullable=False, default=datetime.utcnow)
    

    def __init__(self, Role_ID, Role_Name ,Role_Desc, Date_Created=datetime.now()):
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
    Skill_ID = db.Column(db.String(255), primary_key=True)
    Skill_Name = db.Column(db.String(64), nullable=False)
    Skill_Desc = db.Column(db.String(512), nullable=False)
    Date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def json(self):

        return {"Skill_ID": self.Skill_ID , "Skill_Name": self.Skill_Name, "Skill_Desc": self.Skill_Desc}
    
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
    Skill_ID = db.Column(db.String(255), nullable=False, primary_key=True)

    def __init__(self, Skill_ID,Course_ID):
        self.Skill_ID = Skill_ID
        self.Course_ID = Course_ID
 
    def json(self):
        return { "Skill_ID": self.Skill_ID,"Course_ID": self.Course_ID } 

class Role_Assign(db.Model):
    __tablename__ = 'Role_Assignment'
    Role_ID = db.Column(db.String(255), nullable=False, primary_key=True)
    Skill_ID = db.Column(db.String(255), nullable=False, primary_key=True)

    def __init__(self, Role_ID,Skill_ID):
        self.Role_ID = Role_ID
        self.Skill_ID = Skill_ID
 
    def json(self):
        return { "Role_ID": self.Role_ID, "Skill_ID": self.Skill_ID} 





