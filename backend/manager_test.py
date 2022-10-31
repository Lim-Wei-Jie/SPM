import unittest
from manager import Course, Skill, Role, Role_Assign, Staff, Skill_Assign
from db import LJPS_Assignment, LJPS_Course_Assignment


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
            'Role_Desc': 'RPA and BPM'}
        )

class TestStaff(unittest.TestCase):
    def test_to_dict(self):
        s1 = Staff(
            Staff_ID= '1',
            Staff_FName= 'Jane',
            Staff_LName= 'Doe',
            Dept='HR',
            Email="jane@maimai.com",
            System_Role="2")

        
        self.assertEqual(s1.json(), {
            'staffID': '1',
            'Staff_FName': 'Jane',
            'Staff_LName': 'Doe',
            'Department' : 'HR',
            'Email' : 'jane@maimai.com', 
            'System Role' : '2'}
        )

class TestRoleAssign(unittest.TestCase):
    def test_to_dict(self):
        s1 = Role_Assign(
            Role_ID= '1',
            Skill_ID= '1')

        
        self.assertEqual(s1.json(), {
            'Role_ID': '1',
            'Skill_ID': '1'}
        )

class TestSkillAssign(unittest.TestCase):
    def test_to_dict(self):
        s1 = Skill_Assign(
            Course_ID= 'COR3301',
            Skill_ID= '1')

        
        self.assertEqual(s1.json(), {
            'Course_ID': 'COR3301',
            'Skill_ID': '1'}
        )



class LJPS_Test_Assignment(unittest.TestCase):
    def test_to_dict(self):
        s1 = LJPS_Assignment(
            LJPS_ID= '30',
            Role_ID= '1',
            Staff_ID = '130020'
            )

        
        self.assertEqual(s1.json(), {
            'LJPS_ID': '30',
            'Role_ID': '1',
            'Staff_ID' : '130020'}
        )



class LJPS_Course_Test_Assignment(unittest.TestCase):
    def test_to_dict(self):
        s1 = LJPS_Course_Assignment(
            LJPS_ID= '30',
            Course_ID= 'COR0030'
            )

        
        self.assertEqual(s1.json(), {
            'LJPS_ID': '30',
            'Course_ID': 'COR0030'
            }
        )









if __name__ == "__main__":
    unittest.main()


