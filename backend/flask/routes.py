from app import app
from db import *
from flask import request, jsonify


""" @app.route('/index/')
def hello():
    return jsonify(
    {
        "code": 690,
        "message": [skill_assignment.c.keys()]
    }
    ), 404
 """





#https://teamtreehouse.com/community/what-is-the-difference-between-json-and-jsonparse#:~:text=The%20difference%20is%3A,)%20JavaScript%20object(s).




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
    
    
    

@app.route("/skill/<string:Skill_ID>/<string:Skill_Name>/<string:Skill_Desc>/<string:Date_created>", methods=['GET','POST'])
def create_role(Skill_ID,Skill_Name,Skill_Desc,Date_created):

    if (Skill.query.filter_by(Skill_ID = Skill_ID ).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "Skill_ID": Skill_ID,
                    "Skill_Name": Skill_Name,
                    "Skill_Desc": Skill_Desc,
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
                    "Skill_Desc": Skill_Desc,
                    "Date_created":Date_created
                },
                "message": "An error occurred creating the Role."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": new_skill.json()
        }
    ), 201 
    
    

@app.route("/skill/delete/<string:Skill_ID>",methods=['GET', 'DELETE'])
def deleteSkill(Skill_ID):
    skill = Skill.query.filter_by(Skill_ID=Skill_ID).first()
    if skill:
            db.session.delete(skill)
            db.session.commit()
            
            return jsonify(
                {
                    "code": 201,
                    "message": "Delete success"
                } ), 201

    else:
            return jsonify(
                {
                    "code": 404,
                    "message": "Delete unsuccessful"
                } ), 404   
            
            

@app.route('/skill/update/<string:Skill_ID>/<string:Skill_Name>/<string:Skill_Desc>',methods=['PUT'])
def updateSkill(Skill_ID,Skill_Name,Skill_Desc):
    skill = Skill.query.filter_by(Skill_ID=Skill_ID).first()
    

    if skill:
        
        
         if Skill_ID != "":
            #    course.course_name = data['course_name']
            Skill.Skill_ID = Skill_ID
            
         if Skill_Name != "":
            Skill.Skill_Name = Skill_Name
            
            
         if Skill_Desc != "":
            Skill.Skill_Desc = Skill_Desc
            
         db.session.commit()
                
         return jsonify(
         {
                        "code": 200,
                        "data": "skill has been updated successfully"
            }
         )
            
        
    

        #data = request.get_json()
       
        #if data['course_desc'] != "":
        #    course.course_desc = data['course_desc']
        #if data['course_status'] != "":
        #    course.course_status = data['course_status']
        #if data['course_type'] != "":
        #   course.course_type = data['course_type']
           
         
    return jsonify(
        {
            "code": 404,
            "data": {
                "skill": skill
            },
            "message": "course not found."
        }
    ), 404
 
 

@app.route("/Registration")
def get_all_registration():
    #list
    Reglist = Registration.query.all()
    if len(Reglist):
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    
                    #turn python data into javascript object
                    "registration": [Reg.json() for Reg in Reglist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no registration."
        }
    ), 404
    
    

@app.route("/Registration/<string:Staff_ID>")
def get_registration_staff(Staff_ID):
    #list
    Regis = Registration.query.filter_by(Staff_ID = Staff_ID).all()
    if len(Regis):
        return jsonify(
            {
                "code": 200,
                "registration": [Reg.json() for Reg in Regis]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "registration not found."
        }
    ), 404



  

@app.route("/Registration/addRegis/<string:Reg_ID>/<string:Course_ID>/<string:Staff_ID>/<string:Reg_Status>/<string:Completion_Status>",methods=['GET','POST'])
def create_regis(Reg_ID,Course_ID,Staff_ID,Reg_Status,Completion_Status):
    

    
    
    if (Registration.query.filter_by(Reg_ID = Reg_ID).first()):
        return jsonify(
            {
                "code": 464,
                "data": {
                    "reg_id": Reg_ID,
                    "course_id": Course_ID,
                    "staff_id": Staff_ID,
                    "reg_status":Reg_Status,
                    "completion_status":Completion_Status
                },
                "message": "Registration already exists."
            }
        ), 400
 

    #data = request.get_json()
    #print("poopo" + data)
    
   
    
    new_registration = Registration(Reg_ID,Course_ID,Staff_ID,Reg_Status,Completion_Status)


    
    try:
        db.session.add(new_registration)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "reg_id": Reg_ID,
                    "course_id": Course_ID,
                    "staff_id": Staff_ID,
                    "reg_status":Reg_Status,
                    "completion_status":Completion_Status
                   
                },
                "message": "An error occurred creating the registration."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": new_registration.json()
        }
    ), 201 
    
    

#get skills from role_ID
@app.route("/LJAssign/<string:Staff_ID>",methods=['GET'])
def get_skill_list_by_Role(Staff_ID):
    list_ofID = get_course_id_by_role(Staff_ID)
    filtered_list = filter_LJPSID(list_ofID)
    course_list = LJPS_Course_Assignment.query.filter(LJPS_Course_Assignment.LJPS_ID.in_(filtered_list)).all()
    role_list = LJPS_Assignment.query.filter_by(Staff_ID=Staff_ID).all()
    
    
    #print(course_list)
    xz = []
    yz = []
    
    for i in course_list:
        for y in role_list:
            if (y.LJPS_ID == i.LJPS_ID):
                print('yes')
                
                yz.append(y.LJPS_ID)
                yz.append(y.Role_ID)
                yz.append(i.Course_ID)
                
            
                status_c = Registration.query.filter_by(Course_ID=i.Course_ID,Staff_ID=y.Staff_ID).first()
                if (status_c):
                    yz.append(status_c.Completion_Status)
                    yz.append(status_c.Reg_Status)
                else:
                    yz.append("ERROR")
               
                    
                    
                
        xz.append(yz)
        yz=[]
                
    print(xz)
    
    

    

    if course_list:
        return jsonify(
            {
                "code": 200,
                "data": {
                        "deets": [LJPS_Assign for LJPS_Assign in xz]
                        
                }            
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no such skill"
        }
    ), 404

#filter only skillID
def filter_LJPSID(list_of_id):
    list_onlyID = []
    for data in list_of_id:
        #print(data.Skill_ID)
        list_onlyID.append(str(getattr(data,"LJPS_ID")))
        #print(list_onlyID)
    return list_onlyID

#get skill from associative table using role_id
def get_course_id_by_role(Staff_ID):
    role_list = LJPS_Assignment.query.filter_by(Staff_ID=Staff_ID).all()
    if role_list:
        return role_list
    return jsonify(
        {
            "code": 404,
            "message": "There is no such skill"
        }
    ), 404

    
    

@app.route("/LJPS_Assignment")
def get_LJPS_Assignment():
    #list
    LJPS_Assignment_Map = LJPS_Assignment.query.all()
    if len(LJPS_Assignment_Map):
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    
                    #turn python data into javascript object
                    "maps": [LJPS_Assign.json() for LJPS_Assign in LJPS_Assignment_Map]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Skills assigned to Roles."
        } 
    ), 404
    
    




@app.route("/LJPS_Course/<string:LJPS_ID>")
def get_LJPS_Assignment_By_Course(LJPS_ID):
    #list
    LJPS_Assignment_Map_By_Course = LJPS_Course_Assignment.query.filter_by(LJPS_ID=LJPS_ID).all()
    
    
    if len(LJPS_Assignment_Map_By_Course):
        
         
      
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        
                        #turn python data into javascript object
                        "maps": [LJPS_Assign_Course.json() for LJPS_Assign_Course in LJPS_Assignment_Map_By_Course]
                        
                        
                    }
                }
            )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Skills assigned to Roles."
        } 
    ), 404

    
    
    



if __name__ == '__main__':
    app.run(port=5000, debug=True)
