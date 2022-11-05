import unittest 
import flask_testing 
import json 
from backend.routes import app, db, Course, Skill,Role,Skill_Assign,Role_Assign ,Registration,LJPS_Assignment,LJPS_Course_Assignment 
 
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
        
        self.LJPS1 = LJPS_Assignment (LJPS_ID= 27, Staff_ID = '130010',Role_ID  = 7) 
        self.LJPSC1 = LJPS_Course_Assignment (Course_ID= "COR003AZ", LJPS_ID = 13)
        db.session.add(self.LJPS1)
        db.session.add(self.LJPSC1)
        db.session.commit()
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
        d1 = LJPS_Assignment (LJPS_ID= 12, 
            Staff_ID = '130011',
            Role_ID  = 8) 
        request_body = "/AddLJAssign/" + d1.Staff_ID + "/" + str(d1.Role_ID) + "/" + str(d1.LJPS_ID) 

        response = self.client.get(request_body) 
        self.assertEqual(response.json, { 
            'code':201, 
            'data':  'New learning journey created'
                
                })
        
    def test_add_LJ_Fail(self): 
        
        request_body = "/AddLJAssign/" + "130010" + "/" + "7" + "/" + "27"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
                {
                    "code": 201,
                    "message": "learning journey already exist"
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
        
        
    def test_add_LJC_Fail(self): 
        
        request_body = "/AddLJAssignCourse/" + "COR003AZ"+ "/" + "13"
 
        response = self.client.get(request_body) 
 
        self.assertEqual(response.json,
                {
                    "code": 201,
                    "message": "learning journey course already exist"
                })
        
        
class TestDeLJCourse(TestApp): 
    def test_del_LJ_Course(self): 
        d1 = LJPS_Course_Assignment (Course_ID= "COR003A", LJPS_ID = '33') 
        request_body_1 = "/AddLJAssignCourse/" + d1.Course_ID + "/" + str(d1.LJPS_ID)
        response1 = self.client.get(request_body_1)
        if response1 :
            
            
            request_body_2 = "/DeLJAssignCourse/" + d1.Course_ID + "/" + str(d1.LJPS_ID) 
            response = self.client.get(request_body_2) 
            self.assertEqual(response.json, { 
                'code':201, 
                'message':  'course from learning journey has been successfully removed'
                    
                    })
            
    def test_del_LJ_Course_Fail(self): 
       
            
            
        request_body_2 = "/DeLJAssignCourse/" + "130010" + "/" + "23" 
        response = self.client.get(request_body_2) 
        self.assertEqual(response.json, { 
                'code':500, 
                "message": "Course does not exist"
                    
                    })
            
            
            
class TestDeLJ(TestApp): 
    def test_del_LJ(self): 
        d1 = LJPS_Assignment (LJPS_ID= 33, Staff_ID = '130010', Role_ID  = 7) 
        
        
        request_body_1 = "/AddLJAssign/" + d1.Staff_ID + "/" + str(d1.Role_ID) + "/" + str(d1.LJPS_ID)
        response1 = self.client.get(request_body_1)
        
        if response1:
            
            
        
       
            d2 = LJPS_Course_Assignment (LJPS_ID = 33,Course_ID= "COR003A")
            
            request_body_3 = "/AddLJAssignCourse/" + d2.Course_ID + "/" + str(d2.LJPS_ID)
            response2 = self.client.get(request_body_3)
            
            
            if response2: 
                
                request_body_4 = "/DeleteLJAssign/" + d1.Staff_ID + "/" + str(d1.Role_ID) + "/" + d2.Course_ID + "/" + str(d2.LJPS_ID)
                response3 = self.client.get(request_body_4) 
                self.assertEqual(response3.json, { 
                            'code':201, 
                            'data':  'data being removed'
                                
                                })
                
    def test_del_LJ(self): 
        
        
         d1 = LJPS_Assignment (LJPS_ID= 33, Staff_ID = '130010', Role_ID  = 7) 
        
        
         request_body_1 = "/AddLJAssign/" + d1.Staff_ID + "/" + str(d1.Role_ID) + "/" + str(d1.LJPS_ID)
         response1 = self.client.get(request_body_1)
        
         if response1:
            
            
        
       
            d2 = LJPS_Course_Assignment (LJPS_ID = 33,Course_ID= "COR003A")
            
            request_body_3 = "/AddLJAssignCourse/" + d2.Course_ID + "/" + str(d2.LJPS_ID)
            response2 = self.client.get(request_body_3)
            
            
            if response2: 
                
                request_body_4 = "/DeleteLJAssign/" + "130010" + "/" + "13" + "/" + "13" + "/" + "13"
                response3 = self.client.get(request_body_4) 
                self.assertEqual(response3.json, { 
                            "code": 500,
                            "data": {
                                "message":"data not successfully removed"
                            
                            },
                            "message": "No such learning journey"
                            
                            })
       
            
            
         
        


if __name__ == '__main__': 
    unittest.main()