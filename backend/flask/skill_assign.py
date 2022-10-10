from tkinter import CASCADE
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from sqlalchemy.orm import relationship,backref
from sqlalchemy import MetaData
#from db import Course, Skill

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)




#association table 
metadata_obj = MetaData()
skill_assignment = db.Table('skill_assignment',
metadata_obj,
    db.Column('Course_ID', db.String(20), db.ForeignKey(Course.Course_ID)),
    db.Column('Skill_ID', db.Integer, db.ForeignKey(Skill.Skill_ID))
)