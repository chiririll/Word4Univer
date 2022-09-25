import os.path
from abc import ABC, abstractmethod
from io import BytesIO
from os import PathLike

from .. import Word, Path
from ..Info import LabInfo, StudentInfo


class Lab(ABC):
    """ Base class for all labs  """

    info = LabInfo()

    def __init__(self,

                 info: LabInfo,
                 student: StudentInfo,
                 filename: str = __file__,
                 parts_folder: str | PathLike[str] = None,
                 style: str | PathLike[str] = None,
                 **params):
        """
        Base class for all labs
        :param info: Information about lab
        :param student: Student info
        :param filename: __file__ of derived class
        :param parts_folder: Folder with xml steps files
        :param style: Style xml file path
        :param params: Additional params for document
        """

        self.student = student
        self.info = info

        self.__filename = filename
        parts_folder = self.get_path(parts_folder)

        self.__doc_container = BytesIO()

        params['jinja_globals'] = {
            'laba': self.info,
            'student': self.student,
            **params.get('jinja_globals', {})
        }

        self.document = Word.Document(self.__doc_container, style, parts_folder, **params)

    @abstractmethod
    def add_input(self, key: str, value) -> None:
        pass

    @abstractmethod
    def run(self):
        pass

    def get_path(self, file_path: str):
        return Path.get_path(os.path.dirname(self.__filename), file_path)

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
