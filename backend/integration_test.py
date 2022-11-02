import unittest 
import flask_testing 
import json 
from routes import app, db, Course, Skill,Role,Skill_Assign,Role_Assign 
 
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
 
class TestCreateRole(TestApp): 
    def test_create_role(self): 
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
 
if __name__ == '__main__': 
    unittest.main()