from repository.studentRepository import StudentRepository
from domain.dstudent import Student


class StudentService:
    def __init__(self, studentRepository: StudentRepository):
        self.studentRepository = studentRepository

    def getAllStudents(self):
        '''
        gets the entire list of students and returns it to the console
        :return: all the students
        '''
        return self.studentRepository.getAll()

    def getById(self, idStudent):
        '''
        gets an Id and returns the students's information or None
        :param: idStudent: int
        :return: a student/ None
        '''
        return self.studentRepository.getById(idStudent)

    def addStudent(self, idStudent, name, group, lab, grade):
        '''
        gets the atributes of a student and creates a new one
        :param: idStudent: int
        :param: name: str
        :param: group: int
        :param: lab: int
        :param: grade: float
        '''
        student = Student(idStudent, name, group, lab, grade)
        self.studentRepository.add(student)

    def modifyStudent(self, idStudent, nameNew, groupNew, labNew, gradeNew):
        '''
        gets new atributes for modifying a student
        :param: idStudent: int
        :param: nameNew: str
        :param: groupNew: int
        :param: labNew: int
        :param: gradeNew: int
        '''
        student = Student(idStudent, nameNew, groupNew, labNew, gradeNew)
        self.studentRepository.modify(student)

    def deleteStudent(self, idStudent):
        '''
        gets the Id of the student that is about to be deleted
        :param: idStudent: int
        '''
        self.studentRepository.delete(idStudent)

    def assignLab(self, idStudent, lab):
        '''
        gets the Id of the student that is about to get an assignment, and also the lab that
        is going to be assigned
        :param: idStudent: int
        :param: lab: int
        '''
        self.studentRepository.assign(idStudent, lab)

    def giveGrade(self, idStudent, grade):
        '''
        gets the Id of the student that is about to get a grade, and also the grade that
        is going to be given
        :param: idStudent: int
        :param: grade: float
        '''
        self.studentRepository.giveGrade(idStudent, grade)

    def order_alphabetically(self):
        '''

        '''
        entities = self.getAllStudents()
        inorder = sorted(entities, key=lambda d: d.getName())
        return inorder

    def order_by_grade(self):
        entities = self.getAllStudents()
        inorder = sorted(entities, key=lambda d: d.getGrade(), reverse=True)
        return inorder

    def print_under_5(self):
        entities = self.getAllStudents()
        failed = []
        inorder = sorted(entities, key=lambda d: d.getGrade(), reverse=True)
        for i in inorder:
            if i.getGrade() < 5.0:
                failed.append(i)
        return failed