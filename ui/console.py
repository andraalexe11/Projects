from datetime import datetime
from service.studentService import StudentService
from service.labService import LabService
from service.reportService import ReportService


class Console:
    def __init__(self, studentService: StudentService, labService: LabService, reportService: ReportService):
        self.studentService = studentService
        self.labService = labService
        self.reportService = reportService

    def addStudent(self):
        try:
            idStudent = int(input("Enter student's id: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            name = input("Enter student's name: ")
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            group = int(input("Enter student's group: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        lab = 0
        grade = 0
        try:
            self.studentService.addStudent(idStudent, name, group, lab, grade)
            print("The student has been successfully added!")
        except KeyError as ke:
            print(ke)

    def modifyStudent(self):
        try:
            idStudent = int(input("Enter student's id you want to modify: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            nameNew = input("Enter the new name: ")
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            groupNew = int(input("Enter the new group: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        labNew = self.studentService.getById(idStudent).getLab()
        gradeNew = self.studentService.getById(idStudent).getGrade()
        try:
            self.studentService.modifyStudent(idStudent, nameNew, groupNew, labNew, gradeNew)
            print("The student has been successfully modified!")
        except KeyError as ke:
            print(ke)

    def deleteStudent(self):
        try:
            idStudent = int(input("Enter student's id you want to delete: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            self.studentService.deleteStudent(idStudent)
            print("The student has been successfully deleted!")
        except KeyError as ke:
            print(ke)

    def assingLab(self):
        try:
            idStudent = int(input("Enter student's id you want to assign a lab: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            lab = int(input("Enter the lab number you want to assign: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            self.studentService.assignLab(idStudent, lab)
            print("The lab has been successfully assigned to this student!")
        except KeyError as ke:
            print(ke)

    def giveGrade(self):
        try:
            idStudent = int(input("Enter student's id you want to give a grade: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            grade = float(input("Enter the grade you want to give: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            self.studentService.giveGrade(idStudent, grade)
            print("The grade has been successfully set!")
        except KeyError as ke:
            print(ke)

    def addLab(self):
        try:
            idLab = int(input("Enter lab's id: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            lnumber = int(input("Enter lab's number: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            pnumber = int(input("Enter problem's number: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            description = input("Enter the description: ")
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            deadline = datetime(int(input("Enter the deadline's year: ")), int(input("Enter the deadline's month: ")),
                                int(input("Enter the deadline's day: ")), int(input("Enter the deadline's hour: ")))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            self.labService.addLab(idLab, lnumber, pnumber, description, deadline)
            print("The lab has been successfully added!")
        except KeyError as ke:
            print(ke)

    def modifyLab(self):
        try:
            idLab = int(input("Enter lab's id you want to modify: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            lnumberNew = int(input("Enter the new lab's number: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            pnumberNew = int(input("Enter the new problem's number: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            descriptionNew = input("Enter the new description: ")
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            deadlineNew = datetime(int(input("Enter the new deadline's year: ")),
                                   int(input("Enter the new deadline's month: ")),
                                   int(input("Enter the new deadline's day: ")),
                                   int(input("Enter the new deadline's hour: ")))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            self.labService.modifyLab(idLab, lnumberNew, pnumberNew, descriptionNew, deadlineNew)
            print("The lab has been successfully modified!")
        except KeyError as ke:
            print(ke)

    def deleteLab(self):
        try:
            idLab = int(input("Enter lab's id you want to delete: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            self.labService.deleteLab(idLab)
            print("The lab has been successfully deleted")
        except KeyError as ke:
            print(ke)

    def order_alphabetically(self, entities):
        if entities == []:
            print("The list is empty")
        for i in entities:
            print(i)

    def order_by_grade(self, entities):
        if entities == []:
            print("The list is empty. Please add elements into the list before using this option!")
            return
        for i in entities:
            print(i.getName(), i.getGrade())

    def print_under_5(self, entities):
        if entities == []:
            print("There are no students with grades under 5")
            return
        for i in entities:
            print(i.getName(), i.getGrade())

    def print_all(self, entities):
        if entities == []:
            print("The list is empty. Please add elements into the list before using this option!")
            return
        for entity in entities:
            print(entity)

    def print_top_n_labs_average(self):
        try:
            nr = int(input("Please enter the top number of labs you wish to see: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            entities = self.reportService.get_top_avg_labs(nr)
        except KeyError as ke:
            print(ke)
        if entities == []:
            print("There are no grades to execute this task. Please introduce data first!")
            return
        for i in entities:
            print(i)

    def print_top_n_used_labs(self):
        try:
            nr = int(input("Please enter the top number of labs you wish to see: "))
        except ValueError as ve:
            print(ve, "does not represent a valid type of data. Please try again!")
            return
        try:
            entities = self.reportService.get_top_used_labs(nr)
        except KeyError as ke:
            print(ke)
        if entities == []:
            print("There are no labs assigned to execute this task. Please introduce data first!")
            return
        for i in entities:
            print(i)

    def printMenu(self):
        print("1. Add Student")
        print("2. Modify Student")
        print("3. Delete Student")
        print("4. Print all Students")
        print("5. Assign Lab")
        print("6. Add Lab")
        print("7. Modify Lab")
        print("8. Delete Lab")
        print("9. Print all Labs ")
        print("10. Give a Grade")
        print("11. Print Students Alphabetically with Grades")
        print("12. Print Students in Order by Grades ")
        print("13. Print All Students With Grades Under 5")
        print("14. Print Top n Labs With The Highest Grades Average")
        print("15. Print Top n Most Used Labs")
        print("0. Exit")

    def menu(self):
        while True:
            self.printMenu()
            option = input("Enter the option: ")
            if option == "1":
                self.addStudent()
            elif option == "2":
                self.modifyStudent()
            elif option == "3":
                self.deleteStudent()
            elif option == "4":
                self.print_all(self.studentService.getAllStudents())
            elif option == "5":
                self.assingLab()
            elif option == "6":
                self.addLab()
            elif option == "7":
                self.modifyLab()
            elif option == "8":
                self.deleteLab()
            elif option == "9":
                self.print_all(self.labService.getAllLabs())
            elif option == "10":
                self.giveGrade()
            elif option == "11":
                self.order_alphabetically(self.studentService.order_alphabetically())
            elif option == "12":
                self.order_by_grade(self.studentService.order_by_grade())
            elif option == "13":
                self.print_under_5(self.studentService.print_under_5())
            elif option == "14":
                self.print_top_n_labs_average()
            elif option == "15":
                self.print_top_n_used_labs()
            elif option == "0":
                print("Goodbye!")
                break
            else:
                print("Wrong option. Please try again!")


