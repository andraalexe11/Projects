from unittest import TestCase
from service.studentService import StudentService
from repository.studentRepository import StudentRepository

'''def testSAdd():
    studentRepository = StudentRepository()
    studentservice = StudentService(studentRepository)
    studentservice.addStudent(5, "alina", 311, 0, 0)
    students = studentservice.getAllStudents()
    assert students[0].getIdStudent() == 5
    assert students[0].getName() == "alina"
    assert students[0].getGroup() == 311

def testSModify():
    studentRepository = StudentRepository()
    studentservice = StudentService(studentRepository)
    studentservice.addStudent(5, "alina", 311, 0, 0)
    studentservice.modifyStudent(5, "ioana", 312, 0, 0)
    students = studentservice.getAllStudents()
    assert students[0].getIdStudent() == 5
    assert students[0].getName() == "ioana"
    assert students[0].getGroup() == 312

def testSDelete():
    studentRepository = StudentRepository()
    studentservice = StudentService(studentRepository)
    studentservice.addStudent(5, "alina", 311, 0, 0)
    studentservice.deleteStudent(5)
    students = studentservice.getAllStudents()
    assert len(students) == 0

def testSAssign():
    studentRepository = StudentRepository()
    studentservice = StudentService(studentRepository)
    studentservice.addStudent(5, "alina", 311, 0, 0)
    studentservice.assignLab(5, 3)
    students = studentservice.getAllStudents()
    assert students[0].getLab() == 3

def testSGrade():
    studentRepository = StudentRepository()
    studentservice = StudentService(studentRepository)
    studentservice.addStudent(5, "alina", 311, 0, 0)
    studentservice.giveGrade(5, 9.5)
    students = studentservice.getAllStudents()
    assert students[0].getGrade() == 9.5
    '''


class TestStudentService(TestCase):
    def setUp(self):
        self.studentRepository = StudentRepository()
        self.studentService = StudentService(self.studentRepository)
        self.studentService.addStudent(5,"alina",311,0,0)
        self.students = self.studentService.getAllStudents()

    def testSAdd(self):
        self.assertTrue(self.students[0].getIdStudent() == 5, "Student's Id should be 5")
        self.assertTrue(self.students[0].getName() == "alina", "Student's name should be alina")
        self.assertTrue(self.students[0].getGroup() == 311, "Student's group should be 311")

    def testSModify(self):
        self.studentService.modifyStudent(5, "ioana", 312, 0, 0)
        students = self.studentService.getAllStudents()
        self.assertTrue(students[0].getIdStudent() == 5, "Student's Id should be 5")
        self.assertTrue(students[0].getName() == "ioana", "Student's name should be Ioana")
        self.assertTrue(students[0].getGroup() == 312, "Student's group should be 312")

    def testSDelete(self):
        self.studentService.deleteStudent(5)
        students = self.studentService.getAllStudents()
        self.assertTrue(len(students) == 0, "List length should be 0")

    def testSAssign(self):
        self.studentService.assignLab(5, 3)
        students = self.studentService.getAllStudents()
        self.assertTrue(students[0].getLab() == 3, "Student's lab assignment should be 3")

    def testSGrade(self):
        self.studentService.giveGrade(5, 9.5)
        students = self.studentService.getAllStudents()
        self.assertTrue(students[0].getGrade() == 9.5, "Student's grade should be 9.5")

    def testAlphabetically(self):
        self.studentService.addStudent(11, "monica", 412, 0, 0)
        self.studentService.addStudent(13, "caterina", 711, 0, 0)
        inorder = self.studentService.order_alphabetically()
        self.assertTrue(inorder[1].getName() == "caterina", "Second student's name should be caterina")

    def testByGrade(self):
        self.studentService.addStudent(11, "monica", 412, 8, 0)
        self.studentService.addStudent(13, "caterina", 711, 5, 0)
        inorder = self.studentService.order_by_grade()
        self.assertTrue(inorder[1].getName() == "monica", "Second student's name should be monica")

    def testunder5(self):
        self.studentService.addStudent(11, "monica", 412, 8, 0)
        self.studentService.addStudent(13, "caterina", 711, 9, 0)
        inorder = self.studentService.print_under_5()
        self.assertTrue(inorder[0].getName() == "alina", "Student's name should be alina")

