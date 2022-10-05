from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)


class Course(db.Model):
    __tablename__ = 'course'

    Course_ID = db.Column(db.String(20), primary_key=True)
    Course_Name = db.Column(db.String(50), nullable=False)
    Course_Desc = db.Column(db.String(255) , nullable=False)
    Course_Status = db.Column(db.String(15), nullable=False)
    Course_Type = db.Column(db.String(10), nullable=False)
    Course_Category = db.Column(db.String(50), nullable=False) 
  

    def json(self):
        return {"course_id": self.Course_ID, "Course_Name": self.Course_Name, "Course_Desc": self.Course_Desc, "Course_Status": self.Course_Status,"Course_Type": self.Course_Type, "Course_Category":self.Course_Category}

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
