from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)



#https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-sqlalchemy
class Skill(db.Model):
    __tablename__ = 'skill'

    
    Skill_id = db.Column(db.Integer, primary_key=True)
    Skill_name = db.Column(db.String(64), nullable=False)
    Skill_desc = db.Column(db.String(255), nullable=False)
    Date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
   



    def json(self):
        return {"course_id": self.course_id, "course_name": self.course_name, "course_desc": self.course_desc, "course_status": self.course_status}




class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(64), nullable=False)
    course_desc = db.Column(db.String(255), nullable=False)
    course_status = db.Column(db.String(64), nullable=False)
    course_type = db.Column(db.String(64), nullable=False)
    course_category = db.Column(db.String(64), nullable=False)
  

    def json(self):
        return {"course_id": self.course_id, "course_name": self.course_name, "course_desc": self.course_desc, "course_status": self.course_status}
