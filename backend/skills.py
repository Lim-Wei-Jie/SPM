from tkinter import CASCADE
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from sqlalchemy.orm import relationship,backref
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)


#association table + basic models


class Course(db.Model):
    __tablename__ = 'course'

    Course_ID = db.Column(db.String(20), primary_key=True)
    Course_Name = db.Column(db.String(50), nullable=False)
    Course_Desc = db.Column(db.String(255) , nullable=False)
    Course_Status = db.Column(db.String(15), nullable=False)
    Course_Type = db.Column(db.String(10), nullable=False)
    Course_Category = db.Column(db.String(50), nullable=False) 
    children = relationship("Skill", back_populates="parent")
  

    def corsera(self):
        return {"course_id": self.Course_ID, "Course_Name": self.Course_Name, "Course_Desc": self.Course_Desc, "Course_Status": self.Course_Status,"Course_Type": self.Course_Type, "Course_Category":self.Course_Category}



class Skill(db.Model):
    __tablename__ = 'Skill'

    
    Skill_ID = db.Column(db.Integer, primary_key=True)
    Skill_Name = db.Column(db.String(64), nullable=False)
    Skill_Desc = db.Column(db.String(255), nullable=False)
    Date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Course_ID = db.Column(db.String(20), db.ForeignKey("course.Course_ID"))
    parent = relationship("Course", back_populates="children")
 



    def json(self):
        return {"Skill_id": self.Skill_ID , "Skill_name": self.Skill_Name, "Skill_desc": self.Skill_Desc , "Skill_status": self.Date_created,"courseid": self.Course_ID,"Course_Type":self.parent.Course_Type, "Course Name":self.parent.Course_Name}



#https://teamtreehouse.com/community/what-is-the-difference-between-json-and-jsonparse#:~:text=The%20difference%20is%3A,)%20JavaScript%20object(s).
@app.route("/Skill")
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
    
    

@app.route("/addSkill", methods=['GET','POST'])
def create_skillbook():
    
    Skill_name = "Finance"
    Skill_desc = "pivot table"
    Skill_status = "virtual"
    Skill_type = "Sales"
    
    Skill = Skill(Skill_name = Skill_name,Skill_desc = Skill_desc, Skill_status = Skill_status,Skill_type = Skill_type)
    
    try:
        db.session.add(Skill)
        db.session.commit()
        
        return('Skill added successfully')
        
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the Skill."
            }
        ), 500


@app.route("/deleteSkill/<string:Skill_name>", methods=['GET','DELETE'])
def delete_skillbook(Skill_name):
    
    Skill = Skill.query.filter_by(Skill_name=Skill_name).first()
    if Skill:
        db.session.delete(Skill)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Skill_name": Skill_name + 'has been successfully deleted'
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                 "Skill_name": Skill_name
            },
            "message": "Skill not found."
        }
    ), 404
    

@app.route("/updateSkill/<string:Skill_name>", methods=['GET','PUT'])
def update_skillbook(Skill_name):
    Skill = Skill.query.filter_by(Skill_name=Skill_name).first()
    if Skill:
        Skill.Skill_name = 'Fintech'
        Skill.Skill_desc = 'Finance analytics'
        Skill.Skill_status = 'F2F'
        Skill.Skill_type = Skill.Skill_type
        #data = request.get_json()
        #if data['Skill_name'] != "":
        #    Skill.Skill_name = data['Skill_name']
        #if data['Skill_desc'] != "":
        #    Skill.Skill_desc = data['Skill_desc']
        #if data['Skill_status'] != "":
        #    Skill.Skill_status = data['Skill_status']
        #if data['Skill_type'] != "":
        #   Skill.Skill_type = data['Skill_type']
           
        db.session.commit()
        
        return jsonify(
            {
                "code": 200,
                "data": "Skill has been added successfully"
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "isbn13": Skill
            },
            "message": "Skill not found."
        }
    ), 404




#COURSE ROUTES

#https://teamtreehouse.com/community/what-is-the-difference-between-json-and-jsonparse#:~:text=The%20difference%20is%3A,)%20JavaScript%20object(s).
@app.route("/course")
def get_all():
    #list
    courselist = Course.query.all()
    if len(courselist):
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    
                    #turn python data into javascript object
                    "courses": [course.json() for course in courselist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no courses."
        }
    ), 404
    
    

@app.route("/addcourse", methods=['GET','POST'])
def create_book():
    
    
    
    Course_ID = "F9R1C"
    Course_Name = "Finance"
    Course_Desc = "pivot table"
    Course_Status = "virtual"
    Course_Type = "Sales"
    Course_Category = "Infomatics"
    
   
    course = Course(Course_ID = Course_ID , Course_Name = Course_Name , Course_Desc = Course_Desc , Course_Status = Course_Status , Course_Type = Course_Type , Course_Category = Course_Category )
    
    try:
        db.session.add(course)
        db.session.commit()
        
        return('course added successfully')
        
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the course."
            }
        ), 500


@app.route("/deletecourse/<string:Course_Name>", methods=['GET','DELETE'])
def delete_book(Course_Name):
    
    course = Course.query.filter_by(Course_Name=Course_Name).first()
    if course:
        db.session.delete(course)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course_name": Course_Name + 'has been successfully deleted'
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                 "course_name": Course_Name
            },
            "message": "Course not found."
        }
    ), 404
    

@app.route("/updatecourse/<string:Course_Name>", methods=['GET','PUT'])
def update_book(Course_Name):
    course = Course.query.filter_by(Course_Name=Course_Name).first()
    if course:
        course.Course_Name = 'Fintech'
        course.Course_Desc = 'Finance analytics'
        course.Course_Status = 'F2F'
        course.Course_Type = 'Sales'
        course.Course__Category = "technology"
        #data = request.get_json()
        #if data['course_name'] != "":
        #    course.course_name = data['course_name']
        #if data['course_desc'] != "":
        #    course.course_desc = data['course_desc']
        #if data['course_status'] != "":
        #    course.course_status = data['course_status']
        #if data['course_type'] != "":
        #   course.course_type = data['course_type']
           
        db.session.commit()
        
        return jsonify(
            {
                "code": 200,
                "data": "course has been added successfully"
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "course": course
            },
            "message": "course not found."
        }
    ), 404
    
    
    
@app.route("/searchcourse/<string:Course_Name>",methods=['GET'])
def find_by_course(Course_Name):
    course = Course.query.filter_by(Course_Name = Course_Name).first()
    if course:
        return jsonify(
            {
                "code": 200,
                "data": course.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Course not found."
        }
    ), 404
 


if __name__ == '__main__':
    app.run(port=5000, debug=True)
