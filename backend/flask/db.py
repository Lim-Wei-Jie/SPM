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

        return {"Skill_id": self.Skill_ID , "Skill_name": self.Skill_Name, "Skill_desc": self.Skill_Desc , "Skill_status": self.Date_created}




