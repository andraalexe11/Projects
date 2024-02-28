from repository.studentRepository import StudentRepository
from domain.dstudent import Student


class StudentFileRepository(StudentRepository):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.load_data()

    def load_data(self):
        with open(self.file_name) as f:
            for line in f:
                array = line.split(",")
                student = Student(int(array[0]), array[1], int(array[2]), int(array[3]), int(array[4]))
                super().add(student)

    def add(self, student):
        super().add(student)
        with open(self.file_name, "a") as f:
            f.write(str(student.getIdStudent()) + "," + student.getName() + "," + str(student.getGroup()) + "," + str(
                student.getLab()) + "," + str(student.getGrade()) + "\n")

    def delete(self, idStudent):
        super().delete(idStudent)
        students = super().getAll()
        with open(self.file_name, "w") as f:
            for student in students:
                f.write(
                    str(student.getIdStudent()) + "," + student.getName() + "," + str(student.getGroup()) + "," + str(
                        student.getLab()) + "," + str(student.getGrade()) + "\n")

    def modify(self, studentNew):
        super().modify(studentNew)
        students = super().getAll()
        with open(self.file_name, "w") as f:
            for student in students:
                f.write(
                    str(student.getIdStudent()) + "," + student.getName() + "," + str(student.getGroup()) + "," + str(
                        student.getLab()) + "," + str(student.getGrade()) + "\n")

    def assign(self, idStudent, lab):
        super().assign(idStudent, lab)
        students = super().getAll()
        with open(self.file_name, "w") as f:
            for student in students:
                f.write(
                    str(student.getIdStudent()) + "," + student.getName() + "," + str(student.getGroup()) + "," + str(
                        student.getLab()) + "," + str(student.getGrade()) + "\n")

    def grade(self, idStudent, grade):
        super().giveGrade(idStudent, grade)
        students = super().getAll()
        with open(self.file_name, "w") as f:
            for student in students:
                f.write(
                    str(student.getIdStudent()) + "," + student.getName() + "," + str(student.getGroup()) + "," + str(
                        student.getLab()) + "," + str(student.getGrade()) + "\n")