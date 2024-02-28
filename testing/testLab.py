from datetime import datetime
from domain.dlab import Lab
from unittest import TestCase

'''def testLabGetteri():
    lab = Lab(1, 2, 3, "Sum of 2 numbers", datetime(2022, 12, 12, 10))
    assert lab.getIdLab() == 1
    assert lab.getLnumber() == 2
    assert lab.getPnumber() == 3
    assert lab.getDescription() == "Sum of 2 numbers"
    assert lab.getDeadline() ==  datetime(2022, 12, 12, 10)

def testLabSetteri():
    lab = Lab(1, 2, 3, "Sum of 2 numbers", datetime(2022, 12, 12, 10))
    lab.setIdLab(2)
    lab.setLnumber(5)
    lab.setPnumber(8)
    lab.setDescription("Sum of 4 numbers")
    lab.setDeadline( datetime(2022, 11, 12, 9))
    assert lab.getIdLab() == 2
    assert lab.getLnumber() == 5
    assert lab.getPnumber() == 8
    assert lab.getDescription() == "Sum of 4 numbers"
    assert lab.getDeadline() ==  datetime(2022, 11, 12, 9)
'''


class TestLab(TestCase):
    def setUp(self):
        self.lab = Lab(1, 1, 1, "sum", datetime(2022, 12, 11, 10))

    def testLabGetteri(self):
        self.assertTrue(self.lab.getIdLab() == 1, "Lab ID should be 1")
        self.assertTrue(self.lab.getLnumber() == 1, "Lab number should be 1")
        self.assertTrue(self.lab.getPnumber() == 1, "Problem number should be 1")
        self.assertTrue(self.lab.getDescription() == "sum", "Lab description should be sum")
        self.assertTrue(self.lab.getDeadline() == datetime(2022, 12, 11, 10),
                        "Lab deadline should be 2022-12-11 10:00:00")

    def testLabSetteri(self):
        self.lab.setIdLab(2)
        self.lab.setLnumber(5)
        self.lab.setPnumber(8)
        self.lab.setDescription("Sum of 4 numbers")
        self.lab.setDeadline(datetime(2022, 11, 12, 9))
        self.assertTrue(self.lab.getIdLab() == 2, "Lab ID should be 1")
        self.assertTrue(self.lab.getLnumber() == 5, "Lab number should be 1")
        self.assertTrue(self.lab.getPnumber() == 8, "Problem number should be 1")
        self.assertTrue(self.lab.getDescription() == "Sum of 4 numbers", "Lab description should be Sum of 4 numbers")
        self.assertTrue(self.lab.getDeadline() == datetime(2022, 11, 12, 9),
                        "Lab deadline should be 2022-11-12 09:00:00")
