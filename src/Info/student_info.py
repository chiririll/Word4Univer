from ..Name import FullName


class StudentInfo:
    """ Class for representing student (full name and variant) """

    def __init__(self,
                 name: FullName = None,
                 var: int = 0):
        self.variant = var
        self.name = name if name is not None else FullName()

    def __str__(self):
        return self.name
