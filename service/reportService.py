from domain.dto import LabAverageDTOAssembler, LabUsageDTOAssembler
from repository.studentFileRepository import StudentFileRepository
from repository.labFileRepository import LabFileRepository
from domain.dlab import Lab


class ReportService:
    def __init__(self, studentRepository: StudentFileRepository, labRepository: LabFileRepository):
        self.studentRepository = studentRepository
        self.labRepository = labRepository

    def get_top_avg_labs(self, nr):
        lab_dtos = self.create_lab_dto()
        lab_dtos = sorted(lab_dtos, key=lambda x: x.avg, reverse=True)
        return lab_dtos[:nr]

    def create_lab_dto(self):
        lab_dtos = []
        for lab in self.labRepository.getAll():
            students = self.get_students_lab(lab)
            dto = LabAverageDTOAssembler.create_lab_dto(students, lab)
            lab_dtos.append(dto)
        return lab_dtos

    def get_students_lab(self, lab: Lab):
        students = self.studentRepository.getAll()
        filtered = list(filter(lambda sl: sl.lab == lab.getIdLab() and sl.grade > 0, students))
        return filtered

    def create_lab_usage_dto(self):
        lab_use_dto = []
        for lab in self.labRepository.getAll():
            students = self.studentRepository.getAll()
            dto = LabUsageDTOAssembler.create_lab_usage_dto(students, lab)
            lab_use_dto.append(dto)
        return lab_use_dto

    def get_top_used_labs(self, nr):
        lab_use_dtos = self.create_lab_usage_dto()
        lab_use_dtos = sorted(lab_use_dtos, key=lambda x: x.usings, reverse=True)
        return lab_use_dtos[:nr]