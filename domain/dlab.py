from datetime import datetime


class Lab:
    def __init__(self, idLab, lnumber: int, pnumber: int, description: str, deadline: datetime):
        self.idLab = idLab
        self.lnumber = lnumber
        self.pnumber = pnumber
        self.description = description
        self.deadline = deadline

    def getIdLab(self):
        return self.idLab

    def getLnumber(self):
        return self.lnumber

    def getPnumber(self):
        return self.pnumber

    def getDescription(self):
        return self.description

    def getDeadline(self):
        return self.deadline

    def setIdLab(self, idLab):
        self.idLab = idLab

    def setLnumber(self, lnumber):
        self.lnumber = lnumber

    def setPnumber(self, pnumber):
        self.pnumber = pnumber

    def setDescription(self, description):
        self.description = description

    def setDeadline(self, deadline):
        self.deadline = deadline

    def __str__(self):
        return f"Lab ID: {self.idLab}, Lab Number: {self.lnumber}, Problem Number: {self.pnumber}, Description: {self.description}, Deadline: {self.deadline}"

