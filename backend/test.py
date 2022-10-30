import unittest
from manager import Course,Skill, Role, Role,Role_Assign,Role,Role_Assign


class TestCourse(unittest.TestCase):
    def test_to_dict(self):
        c1 = Course(Course_ID='COR020', Course_Name='BPAS',Course_Desc = 'RPA and BPM',Course_Status = 'Active',Course_Type='Internal',Course_Category='Core')
        
        
        self.assertEqual(c1.json(), {
            'Course_ID': 'COR020',
            'Course_Name': 'BPAS',
            'Course_Desc': 'RPA and BPM',
            'Course_Status': 'Active',
            'Course_Type': 'Internal',
            'Course_Category': 'Core'}
        )
class TestSkill(unittest.TestCase):
    def test_to_dict(self):
        s1 = Skill(Skill_ID= 'BPM020',
            Skill_Name= 'Process Modelling',
            Skill_Desc= 'RPA and BPM',
            Date_created='2022-01-21')
        
        self.assertEqual(s1.json(), {
            'Skill_ID': 'BPM020',
            'Skill_Name': 'Process Modelling',
            'Skill_Desc': 'RPA and BPM',
            'Date_created' : '2022-01-21' }
        )


class TestRole(unittest.TestCase):
    def test_to_dict(self):
        s1 = Role(Role_ID= '1',
            Role_Name= 'Process Analyst',
            Role_Desc= 'RPA and BPM',
            Date_Created='2022-01-21')

        
        self.assertEqual(s1.json(), {
            'Role_ID': '1',
            'Role_Name': 'Process Analyst',
            'Role_Desc': 'RPA and BPM',
            'Date_Created' : '2022-01-21' }
        )






if __name__ == "__main__":
    unittest.main()


