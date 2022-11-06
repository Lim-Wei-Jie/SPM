import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


import unittest 
from flask import Flask
import flask_testing 
import json 
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
        self.c1 = Course(Course_ID=2,
            Course_Name="Test_course 2",
            Course_Desc="Test Course 2",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core")
        self.cka1 = Skill_Assign(Skill_ID= 7, 
            Course_ID= 1)
        self.cka2 = Skill_Assign(Skill_ID= 7, 
            Course_ID= 2)        
            

        db.session.add(self.d1)
        db.session.add(self.s1)
        db.session.add(self.skill2)
        db.session.add(self.ra1)
        db.session.add(self.ra2)
        db.session.commit()
        db.create_all()



    def tearDown(self):
        db.session.remove()
        db.drop_all()
 
class TestCreateRole(TestApp): 
    def test_create_role(self): 
        request_body = "/role/create/RoleTest/TestDecs"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json['code'], 
            201)

    #test creation fail
    def test_create_role_duplicate(self): 
 
        request_body = "/role/create/Process Analyst/RPA and BPM"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json, { 
                "code": 400,
                "data": {
                    "Role_Name": "Process Analyst",
                    "Role_Desc": "RPA and BPM"
                },
                "message": "Role already exists."
                })

class TestDeleteRole(TestApp): 
    #test delete role
    def test_delete_role(self): 

        request_body = "/role/delete/60"
 
        response = self.client.delete(request_body) 
 
        self.assertEqual(response.json, { 
            'code':201, 
            "message": "Delete Successful."})
    
    def test_delete_fail(self): 

        request_body = "/role/delete/70"
 
        response = self.client.delete(request_body) 
 
        self.assertEqual(response.json, { 
             "code": 404,
                "message": "Delete unsuccessful as role does not exist."
                })

        
class TestupdateeRole(TestApp): 
    def test_update_role(self): 
        request_body = "/role/update/60/testpass/testpass87656 d75hhfb"
 
        response = self.client.put(request_body) 
 
        self.assertEqual(response.json,
            {
                "code": 201,
                'data':{'Role_Desc': 'testpass87656 d75hhfb', 
                    'Role_ID': "60", 
                    'Role_Name': 'testpass'},
                "message": "Role Updated sucessfully"
            })
    def test_update_role_desc_only(self): 
        request_body = "/role/update/60/Process Analyst/testpass87656 d75hhfb"
 
        response = self.client.put(request_body) 
 
        self.assertEqual(response.json,
            {
                "code": 201,
                'data':{'Role_Desc': 'testpass87656 d75hhfb', 
                    'Role_ID': "60", 
                    'Role_Name': 'Process Analyst'},
                "message": "Role Updated sucessfully"
            })
    
    def test_update_role_name_only(self): 
        request_body = "/role/update/60/test11/RPA and BPM"
 
        response = self.client.put(request_body) 
 
        self.assertEqual(response.json,
            {
                "code": 201,
                'data':{'Role_Desc': 'RPA and BPM', 
                    'Role_ID': "60", 
                    'Role_Name': 'test11'},
                "message": "Role Updated sucessfully"
            })

    def test_update_role_name_duplicate(self): 
        request_body = "/role/update/60/Process Analyst/RPA and BPM"
 
        response = self.client.put(request_body) 
 
        self.assertEqual(response.json,
            {
                "code": 400,
                "data": {
                    "Role": "Process Analyst",
                    "Role_Desc": "RPA and BPM"
                },
                "message": "Role Duplicate"
            })


    def test_update_role_fail(self): 
        request_body = "/role/update/660/testpass/testpass"
 
        response = self.client.put(request_body) 
 
        self.assertEqual(response.json,
            {
            
                "code": 500,
                "data": {
                    "Role": 'testpass'
                },
                "message": "Role does not exist"
            
            })
class TestgetRolebyid(TestApp): 
    def test_get_role_by_id(self): 
        request_body = "/role/60"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
            {
                "code": 200,
                "data": {
                    "Role": [{'Role_Desc': 'RPA and BPM', 
                            'Role_ID': "60", 
                            'Role_Name': 'Process Analyst'}]
                }  
            })
    
    def test_get_role_by_id_fail(self): 
        request_body = "/role/6067"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
        {
            "code": 404,
            "message": "There is no such role"
        })

class TestgetRolebyname(TestApp): 
    def test_get_role_by_name(self): 
        request_body = "/role/name/Process"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
            {
                "code": 200,
                "data": {
                    "Role": [{'Role_Desc': 'RPA and BPM', 
                            'Role_ID': "60", 
                            'Role_Name': 'Process Analyst'}]
                }  
            })
    def test_get_role_by_name_fail(self): 
        request_body = "/role/name/Process34245thfgh"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
        {
            "code": 404,
            "message": "There is no such role"
        })
class TestGetSkillListbyRole(TestApp): 
    def test_get_skill_list_by_role(self): 
        request_body = "/role/getskill/60"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
            {
                "code": 200,
                "data": {
                    "Skill": [
                    {'Skill_Desc': 'Skill TEst 1', 
                    'Skill_ID': "7", 
                    'Skill_Name': 'Skill TEst 1'},
                    {'Skill_Desc': 'Skill TEst 2', 
                    'Skill_ID': "8", 
                    'Skill_Name': 'Skill TEst 2'}]
                }  
            })
    def test_get_skill_list_by_role_fail(self): 
        request_body = "/role/getskill/6067"

        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
            {
                "code": 404,
                "message": "There is no such skill"
            })

class TestAssignSkilltoRole(TestApp): 
    def test_assign_skill_list_by_role(self): 
        request_body = "/role/roleassignskills/60/[9,20]"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
            {
                "code": 201,
                "data": "['9', '20']"
            })

class TestDeleteSkilltoRole(TestApp): 
    def test_delete_skill_list_by_role(self): 
        request_body = "/role/roledeleteskills/60/[7,8]"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
            {
                "code": 201,
                "data": "['7', '8']"
            })
    
    def test_delete_skill_list_by_role_fail(self): 
        request_body = "/role/roledeleteskills/6440/[7,8]"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
                {
                    "code": 404,
                    "message": "Delete unsuccessful as role does not exist."
                })
    
    

 
 

    def get_course_from_skill_list(self): 
        request_body = "/skill/getcourse/7"
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
    


 
if __name__ == '__main__': 
    unittest.main()