from repository.labRepository import LabRepository
from domain.dlab import Lab


class LabService:
    def __init__(self, labRepository: LabRepository):
        self.labRepository = labRepository

    def getAllLabs(self):
        '''
        gets the entire list of labs and returns it to the console
        '''
        return self.labRepository.getAll()

    def addLab(self, idLab, lnumber, pnumber, description, deadline):
        '''
         gets the atributes of a lab and creates a new one
        :param: idLab: int
        :param: lnumber: int
        :param: pnumber: int
        :param: description: str
        :param: deadline: datetime
        '''
        lab = Lab(idLab, lnumber, pnumber, description, deadline)
        self.labRepository.add(lab)

    def modifyLab(self, idLab, lnumberNew, pnumberNew, descriptionNew, deadlineNew):
        '''
        gets new atributes for modifying a lab
        :param: idLab: int
        :param: lnumberNew: int
        :param: pnumberNew: int
        :param: descriptionNew: str
        :param: deadlineNew: datetime
        '''
        lab = Lab(idLab, lnumberNew, pnumberNew, descriptionNew, deadlineNew)
        self.labRepository.modify(lab)

    def deleteLab(self, idLab):
        '''
        gets the ID of the lab that is about to be deleted
        :param: idLab: int
        '''
        self.labRepository.delete(idLab)