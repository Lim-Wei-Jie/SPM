import unittest 
from flask import Flask
import flask_testing 
import json 
#from manager import app, db, Course, Skill,Role,Skill_Assign,Role_Assign
from backend.routes import app,db, Course, Skill,Role,Skill_Assign,Role_Assign
import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class TestApp(flask_testing.TestCase): 
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://" 
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {} 
    app.config['TESTING'] = True   # 
    app.config['WTF_CSRF_ENABLED'] = False  # 
 
    def create_app(self):
        return app

    def setUp(self):
        db.session.remove()
        db.drop_all()
        db.create_all()
        self.d1 = Role(Role_ID= '60', 
            Role_Name= 'Process Analyst', 
            Role_Desc= 'RPA and BPM')
        self.s1 = Skill(Skill_ID= 8, 
            Skill_Name= 'Skill TEst 2', 
            Skill_Desc= 'Skill TEst 2')
        self.skill2 = Skill(Skill_ID= 7, 
            Skill_Name= 'Skill TEst 1', 
            Skill_Desc= 'Skill TEst 1')
        self.ra1 = Role_Assign(Skill_ID= 7, 
            Role_ID= 60)
        self.ra2 = Role_Assign(Skill_ID= 8, 
            Role_ID= 60)

        self.c1 = Course(Course_ID=1,
            Course_Name="Test_course 1",
            Course_Desc="Test Course 1",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core")
        self.c2 = Course(Course_ID=2,
            Course_Name="Test_course 2",
            Course_Desc="Test Course 2",
            Course_Status="nmj",
            Course_Type="k876",
            Course_Category="vnn")
        self.cka1 = Skill_Assign(Skill_ID= 7, 
            Course_ID= 1)
        self.cka2 = Skill_Assign(Skill_ID= 7, 
            Course_ID= 2)        
            

        db.session.add(self.d1)
        db.session.add(self.s1)
        db.session.add(self.skill2)
        db.session.add(self.ra1)
        db.session.add(self.ra2)
        db.session.add(self.c1)
        db.session.add(self.c2)
        db.session.add(self.cka1)
        db.session.add(self.cka2)

        db.session.commit()
        db.create_all()



    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestCreateSkill(TestApp): 
    def test_create_Skill(self): 
        d1 = Skill(Skill_ID= 6, 
            Skill_Name= 'Business Process Analysis and Modelling', 
            Skill_Desc= 'Signavio',
            Date_created="10/11/2022") 

        request_body = "/skill/"+str(d1.Skill_ID)+"/"+d1.Skill_Name+"/"+d1.Skill_Desc
 
        response = self.client.get(request_body) 
        self.assertEqual(response.json, { 
            'code':201, 
            'data':{ 
                'Skill_Desc': 'Signavio', 
                'Skill_ID': 6, 
                'Skill_Name': 'Business Process Analysis and Modelling'
                }}) 

    def test_create_Skill_duplicate(self): 

        request_body = "/skill/7/Skill TEst 1/Skill TEst 1"

 
        response = self.client.get(request_body) 
        self.assertEqual(response.json, { 
                "code": 400,
                "data": {
                    "Skill_ID": "7",
                    "Skill_Name": "Skill TEst 1",
                    "Skill_Name": "Skill TEst 1"
                },
                "message": "Skill already exists."
            }) 

class testCourseListfromSkill(TestApp): 
    def test_get_courselist_from_Skill(self): 

        request_body = "/skill/getcourse/7"
 
        response = self.client.get(request_body) 
        self.assertEqual(response.json, {
                "code": 200,
                "data": {
                    "Course": [{'Course_Category': 'Core', 
                'Course_Desc': 'Test Course 1', 
                'Course_ID': 1, 
                'Course_Name': 
                'Test_course 1', 
                'Course_Status': 'Active', 
                'Course_Type': 'Internal'}, 
                {'Course_Category': 'vnn', 
                'Course_Desc': 'Test Course 2', 
                'Course_ID': 2, 'Course_Name': 
                'Test_course 2', 'Course_Status': 
                'nmj', 'Course_Type': 'k876'}]}
                }  
            ) 

    def test_get_courselist_from_Skill_fail(self): 

        request_body = "/skill/getcourse/100"
 
        response = self.client.get(request_body) 
        self.assertEqual(response.json,{
            "code": 404,
            "message": "There is no course"
        }) 

class testfindCourseByName(TestApp):
    def test_get_course_from_name(self): 
        request_body = "/searchcourse/Test_course 1"
 
        response = self.client.get(request_body) 
        self.assertEqual(response.json,{
                "code": 200,
                "data": {'Course_Category': 'Core', 
                'Course_Desc': 'Test Course 1', 
                'Course_ID': 1, 
                'Course_Name': 
                'Test_course 1', 
                'Course_Status': 'Active', 
                'Course_Type': 'Internal'}
            }) 

    def test_get_course_from_name_fail(self): 

        request_body = "/searchcourse/notexistenxe"
 
        response = self.client.get(request_body) 
        self.assertEqual(response.json,{
            "code": 404,
            "message": "Course not found."
        }) 

class TestAssignCoursetoSkill(TestApp): 
    def test_assign_course_list_to_skill(self): 
        request_body = "/skill/7/[3,4]"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
            {
                "code": 201,
                "data": "['3', '4']"
            })
    def test_assign_course_list_to_duplicate(self): 
        request_body = "/skill/7/[1,4]"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
            {
                    "code": 400,
                    "data": {
                        
                        "Skill_ID": "7",
                        "Course_ID": "1"
                        
                    },
                    "message": "Skill-course already exists."
            })

class TestDeleteCoursetoSkill(TestApp): 
    def test_Delete_course_list_to_skill(self): 
        request_body = "/skill/skilldeletecourse/7/[1,2]"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
            {
                "code": 201,
                "data": "['1', '2']"
            })
    def test_delete_course_list_to_duplicate(self): 
        request_body = "/skill/skilldeletecourse/7/[66,4]"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
                {
                    "code": 404,
                    "message": "Delete unsuccessful as course does not exist."
                })

class TestDeleteSkill(TestApp): 
    def test_delete_Skill(self): 

        request_body = "/skill/delete/7"
 
        response = self.client.delete(request_body) 
        self.assertEqual(response.json,{
                "code": 201,
                "message": "Delete Successful."
            })

    def test_delete_Skill_fail(self): 

        request_body = "/skill/delete/98"
 
        response = self.client.delete(request_body) 
        self.assertEqual(response.json,            {
                "code": 404,
                "message": "Delete unsuccessful as skill does not exist."
            })

class TestDeleteSkill(TestApp): 
    def test_delete_Skill(self): 

        request_body = "/skill/delete/7"
 
        response = self.client.delete(request_body) 
        self.assertEqual(response.json,{
                "code": 201,
                "message": "Delete Successful."
            })

    def test_delete_Skill_fail(self): 

        request_body = "/skill/delete/98"
 
        response = self.client.delete(request_body) 
        self.assertEqual(response.json,            {
                "code": 404,
                "message": "Delete unsuccessful as skill does not exist."
            })
 
class TestUpdateSkill(TestApp): 
    def test_update_Skill(self): 

        request_body = "/skill/update/7/TEstupdate/TEstupdateduiy"
 
        response = self.client.put(request_body) 
        self.assertEqual(response.json,            {
                "code": 201,
                "data": {'Skill_Desc': 'TEstupdateduiy', 
                    'Skill_ID': 7, 
                    'Skill_Name': 'TEstupdate'},
                "message": "Role Updated sucessfully"
            } )

    def test_delete_Skill_fail(self): 

        request_body = "/skill/update/90/TEstupdate/TEstupdateduiy"
 
        response = self.client.put(request_body) 
        self.assertEqual(response.json,{
                "code": 500,
                "data": {
                    "Skill": "TEstupdate"
                },
                "message": "Role does not exist"
            }) 
if __name__ == '__main__': 
    unittest.main()