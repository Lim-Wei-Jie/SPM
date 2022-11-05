import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from backend.app import app
from backend.db import *
from flask import request, jsonify
import json

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
def get_LJ_by_Staff(Staff_ID):
    list_ofID = get_ljps_id_by_role(Staff_ID)
    filtered_list = filter_LJPSID(list_ofID)
    course_list = LJPS_Course_Assignment.query.filter(LJPS_Course_Assignment.LJPS_ID.in_(filtered_list)).all()
    role_list = LJPS_Assignment.query.filter_by(Staff_ID=Staff_ID).all()
    
    
    #print(course_list)
    xz = []
    yz = []
    
    for i in course_list:
        for y in role_list:
            if (y.LJPS_ID == i.LJPS_ID):
                #print('yes')
                
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
                
    #print(xz)
    
    
  
    spare_list=[]
    master_list=[]
    
    dicts = {}
    keys = range(40)
    values = xz
    for i in keys:
        spare_list=[]
        for j in values:
            if j[1] == i:
                spare_list.append(j)
        dicts[i] = spare_list
    print(dicts)
    #print(xz)
    
    
   
    if course_list:
        return jsonify(
            {
                "code": 200,
                "data": {
                        "deets": dicts
                        
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
def get_ljps_id_by_role(Staff_ID):
    role_list = LJPS_Assignment.query.filter_by(Staff_ID=Staff_ID).all()
    if role_list:
        return role_list
    return jsonify(
        {
            "code": 404,
            "message": "There is no such skill"
        }
    ), 404
    

#get skills from role_ID
@app.route("/AddLJAssign/<string:Staff_ID>/<string:Role_ID>/<string:LJPS_ID>",methods=['GET','POST'])
def Add_LJ_by_Staff(Staff_ID,Role_ID,LJPS_ID):
    

       
        check_staff = LJPS_Assignment.query.filter_by(Staff_ID=Staff_ID,Role_ID = Role_ID).first()
        
        
        if check_staff:
        
                        return jsonify(
                                {
                                    "code": 201,
                                    "message": "learning journey already exist"
                                }
                            ), 201 
                    
        else:
                    

                        
                        new_ljps_assignment = LJPS_Assignment(LJPS_ID,Staff_ID,Role_ID)
                        
                        
                        
                        try:
                            db.session.add(new_ljps_assignment)
                            db.session.commit()
                        except:
                            return jsonify(
                                {
                                    "code": 500,
                                    "data": {
                                        "message":"data not successfully added"
                                    
                                    },
                                    "message": "An error occurred creating the registration."
                                }
                            ), 500
                        
                        return jsonify(
                            {
                                "code": 201,
                                "data": "New learning journey created"
                            }
                        ), 201 
                        
                        
#get skills from role_ID
@app.route("/AddLJAssignCourse/<string:Course_ID>/<string:LJPS_ID>",methods=['GET','POST'])
def Add_Course_by_LJ(Course_ID,LJPS_ID):
    

       
        add_course = LJPS_Course_Assignment.query.filter_by(Course_ID =Course_ID,LJPS_ID = LJPS_ID).all()
        
        
        if add_course:
        
                        return jsonify(
                                {
                                    "code": 201,
                                    "message": "learning journey course already exist"
                                }
                            ), 201 
                    
        else:
                    

                        
                        new_course_assignment = LJPS_Course_Assignment(LJPS_ID,Course_ID)
                        
                        try:
                            db.session.add(new_course_assignment)
                            db.session.commit()
                        except:
                            return jsonify(
                                {
                                    "code": 500,
                                    "data": {
                                        "message":"data not successfully added"
                                    
                                    },
                                    "message": "An error occurred adding the course."
                                }
                            ), 500
                        
                        return jsonify(
                            {
                                "code": 201,
                                "data": "Course added to learning journey"
                            }
                        ), 201 
                        
                        
            

#get skills from role_ID
@app.route("/DeLJAssignCourse/<string:Course_ID>/<string:LJPS_ID>",methods=['GET','DELETE'])
def Del_Course_by_LJ(Course_ID,LJPS_ID):
    

       
        del_course = LJPS_Course_Assignment.query.filter_by(Course_ID=Course_ID,LJPS_ID = LJPS_ID).first()
        
        
        if del_course:
            
            
                        try:
                            
                             db.session.delete(del_course)
                             db.session.commit()
                            
                        except:
                            return jsonify(
                                {
                                    "code": 201,
                                    "data": {
                                        "message":"data not successfully removed"
                                    
                                    },
                                    "message": "An error occurred removing the course."
                                }
                            ), 500
        
                        return jsonify(
                                {
                                    "code": 201,
                                    "message": "course from learning journey has been successfully removed"
                                }
                            ), 201 
                    
        else:
                        
                        return jsonify(
                            {
                                "code": 500,
                                "message": "Course does not exist"
                            }
                        ), 201 
                        
                                   
           
                
               

   

#get skills from role_ID
@app.route("/DeleteLJAssign/<string:Staff_ID>/<string:Role_ID>/<string:Course_ID>/<string:LJPS_ID>",methods=['GET','DELETE'])
def Delete_LJ_by_Staff(Staff_ID,Role_ID,Course_ID,LJPS_ID):
    



        
        staff_list = LJPS_Assignment.query.filter_by(Staff_ID=Staff_ID).all()
        
        if staff_list:
            
            check_course_assignment = LJPS_Course_Assignment.query.filter_by(LJPS_ID=LJPS_ID,Course_ID=Course_ID).first()
    
    
            if check_course_assignment:
                
                try:
                
                    
                    db.session.delete(check_course_assignment)
                    db.session.commit()
                
                except:
                    
                    return jsonify(
                            {
                                "code": 201,
                                "data": "DATA ERROR"
                            }
                        ), 201

                return jsonify(
                    {
                        "code": 201,
                        "data": "data being removed"
                    }
                ), 201 
                    
   
            else:
                
                    return jsonify(
                        {
                            "code": 500,
                            "data": {
                                "message":"data not successfully removed"
                            
                            },
                            "message": "No such learning journey"
                        }
                    ), 500
        
        
                    
            
            
        job_check = LJPS_Assignment.query.filter_by(LJPS_ID=LJPS_ID,Staff_ID=Staff_ID,Role_ID=Role_ID).first()
            
        
            
        if job_check:
                
                
                try:
                    db.session.delete(job_check)
                    db.session.commit()
                except:
                    return jsonify(
                        {
                            "code": 500,
                            "data": {
                                "reg_id": "data removed successfully"
                            
                            },
                            "message": "An error occurred creating the registration 200."
                        }
                    ), 500
            
                return jsonify(
                    {
                        "code": 201,
                        "data": "data being removed"
                    }
                ), 201 
  
    

    
    

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
    
    
    
    
    
# show all inventory
@app.route("/staff")
def get_all_staff():
    staff_list = Staff.query.all()
    print(staff_list)
    if len(staff_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staffList": [staff.json() for staff in staff_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no staff"
        }
    ), 404

@app.route("/role")
def get_all_role():
    role_List = Role.query.all()
    if len(role_List):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Role": [role.json() for role in role_List]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no role"
        }
    ), 404

@app.route("/role/create/<string:Role_ID>/<string:Role_Name>/<string:Role_Desc>", methods=['GET','POST'])
def create_role(Role_ID,Role_Name,Role_Desc):

    if (Role.query.filter_by(Role_Name=Role_Name).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "Role_ID": Role_ID,
                    "Role_Name": Role_Name,
                    "Role_Desc": Role_Desc
                },
                "message": "Role already exists."
            }
        ), 400
    new_role = Role(Role_ID, Role_Name,Role_Desc,datetime.utcnow())
    try:
        db.session.add(new_role)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "Role_ID": Role_ID,
                    "Role_Name": Role_Name,
                    "Role_Desc": Role_Desc,
                },
                "message": "An error occurred creating the Role."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": new_role.json()
        }
    ), 201

@app.route('/role/delete/<string:Role_ID>',methods=['DELETE'])
def delete_role(Role_ID):
    role = Role.query.filter_by(Role_ID=Role_ID).first()
    if role:
        db.session.delete(role)
        db.session.commit()
                
        return jsonify(
            {
                "code": 201,
                "message": "Delete Successful."
            } ), 201


    else:
        return jsonify(
            {
                "code": 404,
                "message": "Delete unsuccessful as role does not exist."
            } ), 404

#update role by ID
@app.route('/role/update/<string:Role_ID>/<string:Role_Name>/<string:Role_Desc>',methods=['PUT'])
def updateRole(Role_ID,Role_Name,Role_Desc):
    role = Role.query.filter_by(Role_ID=Role_ID).first()

    if role:

        Role.query.filter_by(Role_ID=Role_ID).update(dict(Role_Name=Role_Name,Role_Desc=Role_Desc))

        db.session.commit()
        
        return jsonify(
            {
                "code": 201,
                "data": role.json(),
                "message": "Role Updated sucessfully"
            } ), 201
    
    return jsonify(
            {
                "code": 500,
                "data": {
                    "Role": Role_Name
                },
                "message": "Role does not exist"
            }
        ), 500

#get role from id
@app.route("/role/<string:Role_ID>",methods=['GET'])
def get_role_id(Role_ID):
    role = Role.query.filter_by(Role_ID=Role_ID).first()
    print(role)
    if role:
        return jsonify(
            {
                "code": 200,
                "data": {
                        "Role": [role.json()]
                }            
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no such role"
        }
    ), 404

#get role from name
@app.route("/role/name/<string:role_Name>",methods=['GET'])
def get_role_name(role_Name):
    #role_List = Role.query.filter(Role.Role_Name.like(Role_Name)).all()
    role_List = Role.query.filter(Role.Role_Name.like(f'%{role_Name}%')).all()
    print(role_List)
    if role_List:
        return jsonify(
            {
                "code": 200,
                "data": {
                        "Role": [role.json() for role in role_List]
                }            
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no such role"
        }
    ), 404

#viewing the role_assignment table
@app.route("/role/getskill")
def get_mapped_skill_to_role():
    #list
    Skill_Role_Map = Role_Assign.query.all()
    if len(Skill_Role_Map):
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    
                    #turn python data into javascript object
                    "maps": [Skill_Assign.json() for Skill_Assign in Skill_Role_Map]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Skills assigned to Roles."
        } 
    ), 404

#get skills from role_ID
@app.route("/role/getskill/<string:Role_ID>",methods=['GET'])
def get_skill_list_by_Role(Role_ID):
    list_ofID = get_skill_id_by_role(Role_ID) 
    #check list of ID ##Need to add a validator here to check if it returns a list or error
    print(list_ofID)
    if list_ofID:
        filtered_list = filter_skillID(list_ofID)
        skill_list = Skill.query.filter(Skill.Skill_ID.in_(filtered_list)).all()
        if skill_list:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                            "Skill": [skill.json() for skill in skill_list]
                    }            
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There is no such skill"
            }
        ), 404
    return jsonify(
    {
        "code": 404,
        "message": "There is no such skill"
    }), 404     
#filter only skillID
def filter_skillID(list_of_id):
    list_onlyID = []
    for data in list_of_id:
        #print(data.Skill_ID)
        list_onlyID.append(str(getattr(data,"Skill_ID")))
    return list_onlyID
#get skill from associative table using role_id
def get_skill_id_by_role(Role_ID):
    role_list = Role_Assign.query.filter_by(Role_ID=Role_ID).all()
    if role_list:
        return role_list

#mapping skills to role
@app.route("/role/roleassignskills/<string:Role_ID>/<string:Skill_ID>", methods=['GET','POST'])
def role_to_skill_assignment(Role_ID,Skill_ID):
    Skill_ID = Skill_ID.replace("[","")
    Skill_ID = Skill_ID.replace("]","")
    skill_arr = Skill_ID.split(",")
    if_duplicate_err = ""

    for skill in skill_arr:
        print(skill)
        if (Role_Assign.query.filter(Role_Assign.Role_ID.like(Role_ID),Role_Assign.Skill_ID.like(skill)).first()):
                return jsonify(
                {
                    "code": 400,
                    "data": {
                        
                        "Skill_ID": skill,
                        "Role_ID": Role_ID
                        
                    },
                    "message": "Skill-Role already exists."
                }
            ), 400
        
        new_role_assignment = Role_Assign(Role_ID,skill)
        try:
            db.session.add(new_role_assignment)
            db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,
                    "data": {

                        "Role_ID": Role_ID,
                        "Skill_ID": skill
                        
                    },
                    "message": "An error occurred when assigning the skill to role."
                }
            ), 500
    return jsonify(
        {
            "code": 201,
            "data": str(skill_arr)
        }
    ), 201 

#delete skills from role
@app.route("/role/roledeleteskills/<string:Role_ID>/<string:Skill_ID>", methods=['GET','POST'])
def role_to_skill_delete(Role_ID,Skill_ID):
    
    Skill_ID = Skill_ID.replace("[","")
    Skill_ID = Skill_ID.replace("]","")
    skill_arr = Skill_ID.split(",")

    for skill in skill_arr:
        print(skill)
        role_skill_assignment = Role_Assign.query.filter(Role_Assign.Role_ID.like(Role_ID),Role_Assign.Skill_ID.like(skill)).first()
        if role_skill_assignment:
                db.session.delete(role_skill_assignment)
                db.session.commit()
        else:
            return jsonify(
                {
                    "code": 404,
                    "message": "Delete unsuccessful as role does not exist."
                } ), 404
    return jsonify(
        {
            "code": 201,
            "data": str(skill_arr)
        }
    ), 201 





#for skill-course assignment
@app.route("/skill")
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

@app.route("/skill/<string:Skill_ID>/<string:Skill_Name>/<string:Skill_Desc>", methods=['GET','POST'])
def create_skill(Skill_ID,Skill_Name,Skill_Desc):

    if (Skill.query.filter_by(Skill_Name = Skill_Name ).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "Skill_ID": Skill_ID,
                    "Skill_Name": Skill_Name,
                    "Skill_Name": Skill_Desc
                },
                "message": "Skill already exists."
            }
        ), 400
 
    #data = request.get_json()
    #print("poopo" + data)
    new_skill = Skill(Skill_ID,Skill_Name,Skill_Desc)
 
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
                    "Skill_Name": Skill_Desc
                },
                "message": "An error occurred creating the Skill."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": new_skill.json()
        }
    ), 201 
    
#get courses from skill_ID
@app.route("/skill/getcourse/<string:Skill_ID>",methods=['GET'])
def get_course_list_by_Skill(Skill_ID):
    list_ofID = get_course_id_by_skill(Skill_ID)
    if list_ofID:
        filtered_list = filterID(list_ofID)
        course_list = Course.query.filter(Course.Course_ID.in_(filtered_list)).all()
        if course_list:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                            "Course": [course.json() for course in course_list]
                    }            
                }
            )
    return jsonify(
        {
            "code": 404,
            "message": "There is no course"
        }
    ), 404



#filter only courseID
def filterID(list_of_id):
    list_onlyID = []
    for data in list_of_id:
        list_onlyID.append(str(getattr(data,"Course_ID")))
    return list_onlyID

#get course from associative table using skill_id
def get_course_id_by_skill(Skill_ID):
    skill_list = Skill_Assign.query.filter_by(Skill_ID=Skill_ID).all()
    if skill_list:
        return skill_list    

#viewing the skill_assignment table
@app.route("/skill_course_assignment")
def get_mapped_skill_to_course():
    #list
    Skill_Course_Map = Skill_Assign.query.all()
    if len(Skill_Course_Map):
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    
                    #turn python data into javascript object
                    "maps": [Skill_Assign.json() for Skill_Assign in Skill_Course_Map]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Skills assigned to Courses."
        }
    ), 404


@app.route("/skill/<string:Skill_ID>/<string:Course_ID>", methods=['GET','POST'])
def skill_to_course_assignment(Skill_ID,Course_ID):

    Course_ID = Course_ID.replace("[","")
    Course_ID = Course_ID.replace("]","")
    course_arr = Course_ID.split(",")

    if_duplicate_err = ""
    for course in course_arr:
        if (Skill_Assign.query.filter_by(Skill_ID = Skill_ID ,Course_ID=course).first()):
            return jsonify(
                {
                    "code": 400,
                    "data": {
                        
                        "Skill_ID": Skill_ID,
                        "Course_ID": course
                        
                    },
                    "message": "Skill-course already exists."
                }
            ), 400
        new_skill_assignment = Skill_Assign(Skill_ID,course)
    
        try:
            db.session.add(new_skill_assignment)
            db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,
                    "data": {
                        
                        "Skill_ID": Skill_ID,
                        "Course_ID": Course_ID
                    },
                    "message": "An error occurred when assigning the skill to course."
                }
            ), 500
 
    return jsonify(
        {
            "code": 201,
            "data":str(course_arr)
        }
    ), 201 

#delete skills from role
@app.route("/skill/skilldeletecourse/<string:Skill_ID>/<string:Course_ID>", methods=['GET','POST'])
def course_to_skill_delete(Skill_ID,Course_ID):
    
    Course_ID = Course_ID.replace("[","")
    Course_ID = Course_ID.replace("]","")
    course_arr = Course_ID.split(",")

    for course in course_arr:
        print(course)
        course_skill_assignment = Skill_Assign.query.filter(Skill_Assign.Skill_ID.like(Skill_ID),Skill_Assign.Course_ID.like(course)).first()
        if course_skill_assignment:
                db.session.delete(course_skill_assignment)
                db.session.commit()
        else:
            return jsonify(
                {
                    "code": 404,
                    "message": "Delete unsuccessful as course does not exist."
                } ), 404
    return jsonify(
        {
            "code": 201,
            "data": str(course_arr)
        }
    ), 201 

@app.route('/skill/delete/<string:Skill_ID>',methods=['GET','DELETE'])
def delete_skill(Skill_ID):
    skill = Skill.query.filter_by(Skill_ID=Skill_ID).first()
    if skill:
        db.session.delete(skill)
        db.session.commit()
                
        return jsonify(
            {
                "code": 201,
                "message": "Delete Successful."
            } ), 201
    else:
        return jsonify(
            {
                "code": 404,
                "message": "Delete unsuccessful as skill does not exist."
            } ), 404

@app.route('/skill/update/<string:Skill_ID>/<string:Skill_Name>/<string:Skill_Desc>',methods=['PUT'])
def updateSkill(Skill_ID,Skill_Name,Skill_Desc):
    skill = Skill.query.filter_by(Skill_ID=Skill_ID).first()

    if skill:

        Skill.query.filter_by(Skill_ID=Skill_ID).update(dict(Skill_Name=Skill_Name,Skill_Desc=Skill_Desc))

        db.session.commit()
        
        return jsonify(
            {
                "code": 201,
                "data": skill.json(),
                "message": "Role Updated sucessfully"
            } ), 201
    
    return jsonify(
            {
                "code": 500,
                "data": {
                    "Skill": Skill_Name
                },
                "message": "Role does not exist"
            }
        ), 500


    
    
    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
