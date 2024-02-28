from dataclasses import dataclass
from domain.dlab import Lab


@dataclass
class LabAverageDTO:
    number: int
    avg: float


class LabAverageDTOAssembler:
    @staticmethod
    def create_lab_dto(students: list, lab: Lab):
        number = lab.idLab
        n = len(students)
        if not n:
            return LabAverageDTO(0, 0)
        sum = 0
        for i in students:
            sum = sum + i.grade

        avg = sum / n
        return LabAverageDTO(number, avg)


@dataclass
class LabUsageDTO:
    number: int
    usings: int


class LabUsageDTOAssembler:
    @staticmethod
    def create_lab_usage_dto(students: list, lab: Lab):
        number = lab.idLab
        usings = 0
        for i in students:
            if i.lab == number:
                usings += 1
        return LabUsageDTO(number, usings)


