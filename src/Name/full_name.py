class FullName:
    """ Class for storing names """
    def __init__(self,
                 surname: str = "Иванов",
                 name: str = "Иван",
                 patronymic: str = "Иванович"):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def __str__(self):
        return ' '.join([self.surname, self.name, self.patronymic])
