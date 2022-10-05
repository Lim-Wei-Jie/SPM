from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/course'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)


class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(64), nullable=False)
    course_desc = db.Column(db.String(64), nullable=False)
    course_status = db.Column(db.String(64), nullable=False)
    course_type = db.Column(db.String(64), nullable=False)
  

    def json(self):
        return {"course_id": self.course_id, "course_name": self.course_name, "course_desc": self.course_desc, "course_status": self.course_status}

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
    
    

@app.route("/addcourse", methods=['GET','POST'])
def create_book():
    
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
def delete_book(course_name):
    
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
def update_book(course_name):
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
 


if __name__ == '__main__':
    app.run(port=5000, debug=True)
