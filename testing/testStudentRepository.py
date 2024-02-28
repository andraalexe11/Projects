import unittest
from repository.studentRepository import StudentRepository
from domain.dstudent import Student
from unittest import TestCase

'''def testStudentAdd():
    studentRepository = StudentRepository()
    student = Student(1, "Alina", 111, 8, 7.9)
    studentRepository.add(student)
    students = studentRepository.getAll()
    assert len(students) == 1
    assert students[0].getIdStudent() == 1

def testStudentModify():
    studentRepository = StudentRepository()
    student = Student(1, "Alina", 111, 7, 7.9)
    studentRepository.add(student)
    students = studentRepository.getAll()
    studentNew = Student(1,"Ioana", 112, 7, 7.9)
    studentRepository.modify(studentNew)
    students = studentRepository.getAll()
    assert students[0].getName() == "Ioana"

def testStudentDelete():
    studentRepository = StudentRepository()
    student = Student(1, "Alina", 111, 8, 6.5)
    studentRepository.add(student)
    students = studentRepository.getAll()
    studentRepository.delete(1)
    students = studentRepository.getAll()
    assert len(students) == 0

def testStudentAssign():
    studentRepository = StudentRepository()
    student = Student(1, "Alina", 111, 0, 0)
    studentRepository.add(student)
    studentRepository.assign(1, 3)
    assert student.getLab() == 3


def testStudentGrade():
    studentRepository = StudentRepository()
    student = Student(1, "Alina", 111, 0, 0)
    studentRepository.add(student)
    studentRepository.giveGrade(1, 9.5)
    assert student.getGrade() == 9.5
'''


class TestStudentRepository(TestCase):
    def setUp(self):
        self.studentRepository = StudentRepository()
        self.student = Student(1, "Alina", 111, 8, 7.9)
        self.studentRepository.add(self.student)
        self.students = self.studentRepository.getAll()

    def test_StudentAdd(self):
        self.assertTrue(len(self.students) == 1, "List length should be 1")
        self.assertTrue(self.students[0].getIdStudent() == 1, "Student's Id should be 1")

    def test_StudentModify(self):
        studentNew = Student(1, "Ioana", 112, 7, 7.9)
        self.studentRepository.modify(studentNew)
        students = self.studentRepository.getAll()
        self.assertTrue(students[0].getName() == "Ioana", "Student's name should be Ioana")

    def test_StudentDelete(self):
        self.studentRepository.delete(1)
        students = self.studentRepository.getAll()
        self.assertTrue(len(students) == 0, "List length should be 0")

    def test_StudentAssign(self):
        self.studentRepository.assign(1, 3)
        self.assertTrue(self.student.getLab() == 3, "Student's lab assignment should be 3")

    def test_StudentGrade(self):
        self.studentRepository.giveGrade(1, 9.5)
        self.assertTrue(self.student.getGrade() == 9.5, "Student's grade should be 9.5")


if __name__ == '__main__':
    unittest.main()


