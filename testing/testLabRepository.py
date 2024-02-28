from datetime import datetime
from domain.dlab import Lab
from repository.labRepository import LabRepository
from unittest import TestCase

'''def testLabAdd():
    labrepository = LabRepository()
    lab = Lab(1, 2, 3, "Sum of 3 numbers", datetime(2022, 12, 1, 10))
    labrepository.add(lab)
    labs = labrepository.getAll()
    assert len(labs) == 1
    assert labs[0].getIdLab() == 1

def testLabModify():
    labrepository = LabRepository()
    lab = Lab(1, 2, 3, "Sum of 3 numbers", datetime(2022, 12, 1, 10))
    labrepository.add(lab)
    labs = labrepository.getAll()
    labnew = Lab(1, 4, 7, "Sum of 4 numbers", datetime(2022, 11, 1, 9))
    labrepository.modify(labnew)
    labs = labrepository.getAll()
    assert labs[0].getLnumber() == 4
    labs[0].getPnumber() == 7

def testLabDelete():
    labrepository = LabRepository()
    lab = Lab(1, 2, 3, "Sum of 3 numbers", datetime(2022, 12, 1, 10))
    labrepository.add(lab)
    labrepository.delete(1)
    labs = labrepository.getAll()
    assert len(labs) == 0
'''


class TestLabRepository(TestCase):
    def setUp(self):
        self.lab = Lab(1, 2, 3, "Sum of 3 numbers", datetime(2022, 12, 1, 10))
        self.labrepository = LabRepository()
        self.labrepository.add(self.lab)
        self.labs = self.labrepository.getAll()

    def testLabAdd(self):
        self.assertTrue(len(self.labs) == 1, "List length should be 1")
        self.assertTrue(self.labs[0].getIdLab() == 1, "First element's ID should be 1")

    def testLabModify(self):
        labnew = Lab(1, 4, 7, "Sum of 4 numbers", datetime(2022, 11, 1, 9))
        self.labrepository.modify(labnew)
        labs = self.labrepository.getAll()
        self.assertTrue(labs[0].getLnumber() == 4, "First element's lab number should be 4")
        self.assertTrue(labs[0].getPnumber() == 7, "First element's problem number should be 7")

    def testLabDelete(self):
        self.labrepository.delete(1)
        labs = self.labrepository.getAll()
        self.assertTrue(len(labs) == 0, "List length should be 0")






