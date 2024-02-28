from service.studentService import StudentService
from service.labService import LabService
from ui.console import Console
from repository.studentFileRepository import StudentFileRepository
from repository.labFileRepository import LabFileRepository
from service.reportService import ReportService

def main():
    studentRepository = StudentFileRepository("C:\\Users\\Alexe Andra\\PycharmProjects\\Lab 7-9\\students.txt")
    labRepository = LabFileRepository("C:\\Users\\Alexe Andra\\PycharmProjects\\Lab 7-9\\labs.txt")
    studentService = StudentService(studentRepository)
    labService = LabService(labRepository)
    reportService = ReportService(studentRepository, labRepository)
    console = Console(studentService, labService, reportService)
    console.menu()

main()