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



#indiv models 
class Course(db.Model):
    __tablename__ = 'course'

    Course_ID = db.Column(db.String(20), primary_key=True)
    Course_Name = db.Column(db.String(50), nullable=False)
    Course_Desc = db.Column(db.String(255) , nullable=False)
    Course_Status = db.Column(db.String(15), nullable=False)
    Course_Type = db.Column(db.String(10), nullable=False)
    Course_Category = db.Column(db.String(50), nullable=False)
    #Skills = relationship("Skill", secondary=skill_assignment)

    def json(self):

        return {"course_id": self.Course_ID, "Course_Name": self.Course_Name, "Course_Desc": self.Course_Desc, "Course_Status": self.Course_Status,"Course_Type": self.Course_Type, "Course_Category":self.Course_Category}

class Skill(db.Model):

    __tablename__ = 'Skill'
    
    Skill_ID = db.Column(db.Integer, primary_key=True)
    Skill_Name = db.Column(db.String(64), nullable=False)
    Skill_Desc = db.Column(db.String(255), nullable=False)
    Date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
   #Courses = relationship("Course", secondary=skill_assignment)
    def json(self):

        return {"Skill_id": self.Skill_ID , "Skill_name": self.Skill_Name, "Skill_desc": self.Skill_Desc , "Date_created": self.Date_created}
    
    
    def __init__(self, Skill_ID, Skill_Name, Skill_Desc, Date_created=None):
        self.Skill_ID = Skill_ID 
        self.Skill_Name = Skill_Name
        self.Skill_Desc = Skill_Desc
        if Date_created is None:
            self.created_time = datetime.utcnow()
        else:
            self.created_time = Date_created
            
            
class Registration(db.Model):
    __tablename__ = 'registration'

    Reg_ID = db.Column(db.Integer, primary_key=True)
    Course_ID = db.Column(db.String(64), nullable=False)
    Staff_ID = db.Column(db.String(255), nullable=False)
    Reg_Status = db.Column(db.String(64), nullable=False)
    Completion_Status = db.Column(db.String(64), nullable=False)
  

    def json(self):
        return {"reg_id": self.Reg_ID, "course_id": self.Course_ID , "staff_id": self.Staff_ID, "reg_status": self.Reg_Status, "completion_status":self.Completion_Status}
    
    
    def __init__(self, Reg_ID, Course_ID, Staff_ID, Reg_Status,Completion_Status):
        self.Reg_ID = Reg_ID 
        self.Course_ID = Course_ID
        self.Staff_ID = Staff_ID
        self.Reg_Status = Reg_Status
        self.Completion_Status = Completion_Status
    
    

class LJPS_Assignment(db.Model):
    __tablename__ = 'LJPS_Assignment'


    LJPS_ID = db.Column(db.Integer, nullable=False, primary_key=True)
    Staff_ID = db.Column(db.Integer, nullable=False, primary_key=True)
    Role_ID = db.Column(db.Integer, nullable=False, primary_key=True)

    def __init__(self,  LJPS_ID ,Staff_ID ,Role_ID):
        
        
        self.LJPS_ID = LJPS_ID
        self.Staff_ID = Staff_ID
        self.Role_ID = Role_ID
 
    def json(self):
        return { "LJPS_ID": self.LJPS_ID,"Staff_ID": self.Staff_ID, "Role_ID":self.Role_ID} 
    
    


class LJPS_Course_Assignment(db.Model):
    __tablename__ = 'LJPS_Course_Assignment'


    LJPS_ID = db.Column(db.Integer, nullable=False, primary_key=True)
    Course_ID = db.Column(db.String(64), nullable=False, primary_key=True)


    def __init__(self,  LJPS_ID ,Course_ID):
        
        
        self.LJPS_ID = LJPS_ID
        self.Course_ID = Course_ID
 
    def json(self):
        return { "LJPS_ID": self.LJPS_ID,"Course_ID": self.Course_ID} 
    
    


    





