from tkinter import CASCADE
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from sqlalchemy.orm import relationship,backref

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/course1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)


#association table

class Skill_Assignment(db.Model):
    __tablename__ = 'Skill_Assignment'
    skill_assignment_id = db.Column(db.Integer, primary_key=True)
    Course_ID =  db.Column(db.Integer, db.ForeignKey('course.course_id'))  #tablename.id
    Skill_ID = db.Column(db.Integer, db.ForeignKey('Skill.Skill_ID'))

    skill = relationship(Skill, backref=backref("Skill_Assignment", cascade="all, delete-orphan"))
    course = relationship(Course, backref=backref("Skill_Assignment", cascade="all, delete-orphan"))


class Skill(db.Model):
    __tablename__ = 'Skill'

    
    Skill_ID = db.Column(db.Integer, primary_key=True)
    Skill_Name = db.Column(db.String(64), nullable=False)
    Skill_Desc = db.Column(db.String(255), nullable=False)
    Date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    #relationship statement
    courses = relationship("Course", secondary="Skill_Assignment")


    def json(self):
        return {"Skill_id": self.Skill_id, "Skill_name": self.Skill_name, "Skill_desc": self.Skill_desc, "Skill_status": self.Skill_status}



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




class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(64), nullable=False)
    course_desc = db.Column(db.String(64), nullable=False)
    course_status = db.Column(db.String(64), nullable=False)
    course_type = db.Column(db.String(64), nullable=False)
  
    skills = relationship("Skill", secondary="Skill_Assignment")
  
  
    def json(self):
        return {"course_id": self.course_id, "course_name": self.course_name, "course_desc": self.course_desc, "course_status": self.course_status}

#https://teamtreehouse.com/community/what-is-the-difference-between-json-and-jsonparse#:~:text=The%20difference%20is%3A,)%20JavaScript%20object(s).
@app.route("/course")
def get_all_course():
    #list
    courselist = Course.query.all()
    if len(courselist):
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    
                    #turn python data into javascript object
                    "books": [course.json() for course in courselist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no courses."
        }
    ), 404
    
@app.route("/searchcourse/<string:course_name>",methods=['GET'])
def find_by_course(course_name):
    course = Course.query.filter_by(course_name=course_name).first()
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
    

@app.route("/addcourse", methods=['GET','POST'])
def create_coursebook():
    
    course_name = "Finance"
    course_desc = "pivot table"
    course_status = "virtual"
    course_type = "Sales"
    
    course = Course(course_name = course_name,course_desc = course_desc, course_status = course_status,course_type = course_type)
    
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


@app.route("/deletecourse/<string:course_name>", methods=['GET','DELETE'])
def delete_coursebook(course_name):
    
    course = Course.query.filter_by(course_name=course_name).first()
    if course:
        db.session.delete(course)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course_name": course_name + 'has been successfully deleted'
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                 "course_name": course_name
            },
            "message": "Course not found."
        }
    ), 404
    

@app.route("/updatecourse/<string:course_name>", methods=['GET','PUT'])
def update_coursebook(course_name):
    course = Course.query.filter_by(course_name=course_name).first()
    if course:
        course.course_name = 'Fintech'
        course.course_desc = 'Finance analytics'
        course.course_status = 'F2F'
        course.course_type = course.course_type
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
                "isbn13": course
            },
            "message": "course not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)
