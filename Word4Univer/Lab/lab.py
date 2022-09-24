from abc import ABC, abstractmethod
from io import BytesIO

from .. import Word, Path
from ..Info import LabInfo, StudentInfo


class Lab(ABC):
    """ Base class for all labs  """

    def __init__(self, info: LabInfo, student: StudentInfo, **params):
        self.student = student
        self.info = info

        self.__doc_container = BytesIO()

        params['jinja_globals'] = {
            'laba': self.info,
            'student': self.student,
            **params.get('jinja_globals', {})
        }

        self.document = Word.Document(self.__doc_container, **params)

    @abstractmethod
    def add_input(self, key: str, value) -> None:
        pass

    @abstractmethod
    def run(self):
        pass

    def get_container(self) -> BytesIO:
        self.document.save()
        return self.__doc_container

    def save_to_file(self, filename: str = None):
        if filename is None:
            filename = Path.get_wd(f"output/{self.info.subject}/Lab{self.info.index}_v{self.student.variant}.doc")

        Path.Utils.create_folders(filename)

        self.document.save()
        with open(filename, 'wb') as f:
            self.__doc_container.seek(0)
            f.write(self.__doc_container.read())
