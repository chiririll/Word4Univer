from Word4Univer import Lab, LabInfo, StudentInfo, TitlePages

from .Subjects import TestSubject


class PartsLab(Lab):

    info = LabInfo(
        name="Test parts lab",
        index=10,
        theme="Test Lab theme",
        subject=TestSubject
    )

    def __init__(self, student: StudentInfo):
        super().__init__(self.info, student, __file__, "docparts")

    def run(self):
        self.document.add_step("test")
        self.document.add_step("folder/test")

    def add_input(self, key: str, value) -> None:
        pass

