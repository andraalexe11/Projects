from datetime import datetime
from repository.labRepository import LabRepository
from domain.dlab import Lab


class LabFileRepository(LabRepository):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.load_data()

    def load_data(self):
        with open(self.file_name) as f:
            for line in f:
                array = line.split(",")
                lab = Lab(int(array[0]), int(array[1]), int(array[2]), array[3],
                          datetime(int(array[4]), int(array[5]), int(array[6]), int(array[7])))
                super().add(lab)

    def add(self, lab):
        super().add(lab)
        with open(self.file_name, "a") as f:
            f.write(str(lab.getIdLab()) + "," + str(lab.getLnumber()) + "," + str(
                lab.getPnumber()) + "," + lab.getDescription() + "," + str(lab.getDeadline()) + "\n")

    def delete(self, idLab):
        super().delete(idLab)
        labs = super().getAll()
        for lab in labs:
            with open(self.file_name, "w") as f:
                f.write(str(lab.getIdLab()) + "," + str(lab.getLnumber()) + "," + str(
                    lab.getPnumber()) + "," + lab.getDescription() + "," + str(lab.getDeadline()) + "\n")

    def modify(self, labNew):
        super().modify(labNew)
        labs = super().getAll()
        for lab in labs:
            with open(self.file_name, "w") as f:
                f.write(str(lab.getIdLab()) + "," + str(lab.getLnumber()) + "," + str(
                    lab.getPnumber()) + "," + lab.getDescription() + "," + str(lab.getDeadline()) + "\n")

