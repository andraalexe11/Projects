from domain.dlab import Lab


class LabRepository:
    def __init__(self):
        self.labs = {}

    def getAll(self):
        '''
        providing the list of labs
        :return: a lab type list of labs
        '''
        return list(self.labs.values())

    def getByID(self, idLab):
        '''
        searching a lab by lab id
        :param idLab: int
        :return: a lab, if there is one with the given id or None, if there is not
        '''
        if idLab in self.labs:
            return self.labs[idLab]
        return None

    def add(self, lab: Lab):
        '''
        adding a new lab
        :param: lab: Lab
        '''
        if self.getByID(lab.getIdLab()) is not None:
            raise KeyError("There is already a lab with this ID.")
        self.labs[lab.getIdLab()] = lab

    def modify(self, labNew: Lab):
        '''
        modifying a lab's number, description and/or deadline
        :param: labNew: Lab
        '''
        if self.getByID(labNew.getIdLab()) is None:
            raise KeyError("There is no lab with this Id.")
        self.labs[labNew.getIdLab()] = labNew

    def delete(self, idLab):
        '''
        deleting a lab
        :param: idLab: int
        '''
        if self.getByID(idLab) is None:
            raise KeyError("There is no lab with this ID.")
        self.labs.pop(idLab)