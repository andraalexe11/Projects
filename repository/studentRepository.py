from domain.dstudent import Student


class StudentRepository:
    def __init__(self):
        self.students = {}

    def getAll(self):
        '''
        providing the list of students
        :return: a student type list of students
        '''
        return list(self.students.values())

    def getById(self, idStudent):
        '''
        searching a student by id
        :param idStudent: string
        :return: a student, if there is one with thne given id or None, if there is not
        '''
        if idStudent in self.students:
            return self.students[idStudent]
        return None

    def add(self, student: Student):
        '''
        adding a new student into the list
        :param: student: Student
        '''
        if self.getById(student.getIdStudent()) is not None:
            raise KeyError("There is already a student with this id.")
        self.students[student.getIdStudent()] = student

    def modify(self, studentNew: Student):
        '''
        modifying a student's name and/or group
        :param: studentNew: Student
        '''
        if self.getById(studentNew.getIdStudent()) is None:
            raise KeyError("There is no student with this id.")
        self.students[studentNew.getIdStudent()] = studentNew

    def delete(self, idStudent):
        '''
        deleting a student
        :param: idStudent
        '''
        if self.getById(idStudent) is None:
            raise KeyError("There is no student with this id.")
        self.students.pop(idStudent)

    def assign(self, idStudent, lab):
        '''
        assigning a lab to a student
        :param: idStudent
        :param: lab
        '''
        if self.getById(idStudent) is None:
            raise KeyError("There is no student with this id.")
        self.students[idStudent].setLab(lab)

    def giveGrade(self, idStudent, grade):
        '''
        giving a grade to a student
        :param: idStudent
        :param: lab
        '''
        if self.getById(idStudent) is None:
            raise KeyError("There is no student with this id.")
        self.students[idStudent].setGrade(grade)





