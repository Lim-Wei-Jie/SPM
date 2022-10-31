import unittest
import flask_testing
import json
from manager import app, db, Course, Skill,Role,Skill_Assign,Role_Assign

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root@localhost:3306/lms"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            db.session.execute(f"TRUNCATE {table.name} RESTART IDENTITY CASCADE;")
        db.session.remove()
        #db.drop_all()


class TestCreateRole(TestApp):
    def test_create_role(self):
        d1 = Role(Role_ID= '63',
            Role_Name= 'Process Analyst',
            Role_Desc= 'RPA and BPM')

        request_body = "/role/create/"+str(d1.Role_ID)+"/"+d1.Role_Name+"/"+d1.Role_Desc

        request_body2 = "/role"


        response = self.client.get(request_body)

        self.assertEqual(response.json, {
            'code':201,
            'data':{'Role_Desc': 'RPA and BPM',
                'Role_ID': 63,
                'Role_Name': 'Process Analyst'}})

if __name__ == '__main__':
    unittest.main()