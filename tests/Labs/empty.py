from Word4Univer import Lab, LabInfo, StudentInfo


class EmptyLab(Lab):
    def __init__(self, **params):
        super().__init__(LabInfo(), StudentInfo(), **params)

    def add_input(self, key: str, value):
        pass

    def run(self):
        pass
