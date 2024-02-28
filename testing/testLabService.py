from datetime import datetime
from service.labService import LabService
from repository.labRepository import LabRepository
from unittest import TestCase

'''def testLAdd():
    labRepository = LabRepository()
    labService = LabService(labRepository)
    labService.addLab(1, 3, 5, "sum", datetime(2022, 12, 30, 12))
    labs = labService.getAllLabs()
    assert labs[0].getIdLab() == 1
    assert labs[0].getPnumber() == 5
    assert labs[0].getDescription() == "sum"

def testLModify():
    labRepository = LabRepository()
    labService = LabService(labRepository)
    labService.addLab(1, 3, 5, "sum", datetime(2022, 12, 30, 12))
    labService.modifyLab(1, 4, 8, "average", datetime(2022, 12, 24, 15))
    labs = labService.getAllLabs()
    assert labs[0].getIdLab() == 1
    assert labs[0].getPnumber() == 8
    assert labs[0].getDescription() == "average"

def testLDelete():
    labRepository = LabRepository()
    labService = LabService(labRepository)
    labService.addLab(1, 3, 5, "sum", datetime(2022, 12, 30, 12))
    labService.deleteLab(1)
    labs = labService.getAllLabs()
    assert len(labs) == 0
'''


class TestLabService(TestCase):
    def setUp(self):
        self.labRepository = LabRepository()
        self.labService = LabService(self.labRepository)
        self.labService.addLab(1, 3, 5, "sum", datetime(2022, 12, 30, 12))
        self.labs = self.labService.getAllLabs()

    def testLAdd(self):
        self.assertTrue(self.labs[0].getIdLab() == 1, "Lab ID should be 1")
        self.assertTrue(self.labs[0].getPnumber() == 5, "Lab problem number should be 5")
        self.assertTrue(self.labs[0].getDescription() == "sum", "Lab description should be sum")

    def testLModify(self):
        self.labService.modifyLab(1, 4, 8, "average", datetime(2022, 12, 24, 15))
        labs = self.labService.getAllLabs()
        self.assertTrue(labs[0].getIdLab() == 1, "Lab ID should be 1")
        self.assertTrue(labs[0].getPnumber() == 8, "Lab problem number should be 8")
        self.assertTrue(labs[0].getDescription() == "average", "Lab description should be average")

    def testLDelete(self):
        self.labService.deleteLab(1)
        labs = self.labService.getAllLabs()
        self.assertTrue(len(labs) == 0, "List length should be 0")


