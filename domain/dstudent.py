class Student:
    def __init__(self, idStudent, name, group, lab, grade):
        self.idStudent = idStudent
        self.name = name
        self.group = group
        self.lab = lab
        self.grade = grade

    def getIdStudent(self):
        return self.idStudent

    def getName(self):
        return self.name

    def getGroup(self):
        return self.group

    def getLab(self):
        return self.lab

    def getGrade(self):
        return self.grade

    def setIdStudent(self, IdStudent):
        self.idStudent = IdStudent

    def setName(self, name):
        self.name = name

    def setGroup(self, group):
        self.group = group

    def setLab(self, lab):
        self.lab = lab

    def setGrade(self, grade):
        self.grade = grade

    def __str__(self):
        return f"id: {self.idStudent}, name: {self.name}, group: {self.group}, lab: {self.lab}, grade: {self.grade}"





