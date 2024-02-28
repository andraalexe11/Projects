from domain.dstudent import Student
from unittest import TestCase

'''
def testStudentGetteri():
    student = Student(1, "Alina", 311, 3, 8.7)
    assert student.getIdStudent() == 1
    assert student.getName() == "Alina"
    assert student.getGroup() == 311
    assert student.getGrade() == 8.7
    assert student.getLab() == 3

def testStudentSetteri():
    student = Student(1, "Alina", 311, 3, 8.7)
    student.setIdStudent(3)
    student.setGroup(111)
    student.setName("Marcel")
    student.setGrade(6.9)
    student.setLab(6)
    assert student.getIdStudent() == 3
    assert student.getName() == "Marcel"
    assert student.getGroup() == 111
    assert student.getGrade() == 6.9
    assert student.getLab() == 6
'''


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student(1, "Alina", 311, 3, 8.7)

    def testStudentGetteri(self):
        self.assertTrue(self.student.getIdStudent() == 1, "student id should be 1")
        self.assertTrue(self.student.getName() == "Alina", "Student name should be Alina")
        self.assertTrue(self.student.getGroup() == 311, "student group should be 311")
        self.assertTrue(self.student.getGrade() == 8.7, "student grade should be 8.7")
        self.assertTrue(self.student.getLab() == 3, "student lab should be 3")

    def testStudentSetteri(self):
        self.student.setIdStudent(3)
        self.student.setGroup(111)
        self.student.setName("Marcel")
        self.student.setGrade(6.9)
        self.student.setLab(6)
        self.assertTrue(self.student.getIdStudent() == 3, "student id should be 3")
        self.assertTrue(self.student.getName() == "Marcel", "Student name should be Marcel")
        self.assertTrue(self.student.getGroup() == 111, "student group should be 111")
        self.assertTrue(self.student.getGrade() == 6.9, "student grade should be 6.9")
        self.assertTrue(self.student.getLab() == 6, "student lab should be 6")



