import unittest 
import flask_testing 
import json 
from routes import app, db, Course, Skill,Role,Skill_Assign,Role_Assign ,Registration,LJPS_Assignment,LJPS_Course_Assignment 
 
class TestApp(flask_testing.TestCase): 
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://" 
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {} 
    app.config['TESTING'] = True   # 
    app.config['WTF_CSRF_ENABLED'] = False  # 
 
    def create_app(self): 
        return app 
 
    def setUp(self): 
        db.create_all() 
 
    def tearDown(self): 
        db.session.remove() 
        db.drop_all() 
 
class TestCreateLJ(TestApp): 
    def test_create_LJ(self): 
        d1 = Role(Role_ID= '60', 
            Role_Name= 'Process Analyst', 
            Role_Desc= 'RPA and BPM') 
 
        request_body = "/role/create/"+str(d1.Role_ID)+"/"+d1.Role_Name+"/"+d1.Role_Desc  
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json, { 
            'code':201, 
            'data':{'Role_Desc': 'RPA and BPM', 
                'Role_ID': 60, 
                'Role_Name': 'Process Analyst'}}) 
 
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


class TestCreateRegistration(TestApp): 
    def test_create_Regis(self): 
        d1 = Registration(Reg_ID= 6, 
            Course_ID = 'COR0003', 
            Staff_ID = '130002',
            Reg_Status ="Completed",
            Completion_Status = "done") 
        request_body = "/Registration/addRegis/"+str(d1.Reg_ID)+"/"+d1.Course_ID+"/"+d1.Staff_ID + "/" + d1.Reg_Status + "/" + d1.Completion_Status

        response = self.client.get(request_body) 
        self.assertEqual(response.json, { 
            'code':201, 
            'data':{ 
                'Reg_ID': 6, 
                'Course_ID' : 'COR0003', 
                'Staff_ID': '130002',
                'Reg_Status': 'Completed',
                'Completion_Status': 'done'
                }})
        
        
 
        
class TestAddLJ(TestApp): 
    def test_add_LJ(self): 
        d1 = LJPS_Assignment (LJPS_ID= 27, 
            Staff_ID = '130010',
            Role_ID  = 7) 
        request_body = "/AddLJAssign/" + d1.Staff_ID + "/" + str(d1.Role_ID) + "/" + str(d1.LJPS_ID) 

        response = self.client.get(request_body) 
        self.assertEqual(response.json, { 
            'code':201, 
            'data':  'New learning journey created'
                
                })
 
   
        
class TestAddLJCourse(TestApp): 
    def test_add_LJ_Course(self): 
        d1 = LJPS_Course_Assignment (Course_ID= "COR003A", 
            LJPS_ID = '33') 
        request_body = "/AddLJAssignCourse/" + d1.Course_ID + "/" + str(d1.LJPS_ID) 

        response = self.client.get(request_body) 
        self.assertEqual(response.json, { 
            'code':201, 
            'data':  'Course added to learning journey'
                
                })
        


if __name__ == '__main__': 
    unittest.main()