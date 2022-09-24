from .full_name import FullName


class NamePattern:
    """ Pattern for parsing and formatting full name """

    def __init__(self, pattern: str = None):
        """ Initialization """
        if pattern is None:
            pattern = 'SNP'

        self.__positions = []
        self.update_pattern(pattern)

    def update_pattern(self, pattern: str) -> None:
        """
        Method for applying new pattern
        @param pattern: pattern string (S - surname, N - name, P - patronymic)
        """
        self.__positions.clear()
        for pos in pattern.upper():
            if pos == 'S' and 'S' not in self.__positions:
                self.__positions.append('S')
            elif pos == 'N' and 'N' not in self.__positions:
                self.__positions.append('N')
            elif pos == 'P' and 'P' not in self.__positions:
                self.__positions.append('P')
            else:
                raise ValueError(f'Pattern "{pattern}" is not a valid pattern!')

    def get_list(self, full_name: FullName) -> list:
        """
        Method for ordering full name
        @return: List with ordered full name
        """
        items = {'S': full_name.surname, 'N': full_name.name, 'P': full_name.patronymic}
        return list(map(lambda pos: items[pos], self.__positions))

    def get_str(self, fullname: FullName) -> str:
        """
        Method for ordering full name
        @return: String with ordered full name
        """
        return ' '.join(self.get_list(fullname))

    def parse_list(self, *full_name: str) -> FullName:
        """
        Method for parsing list with surname name and patronymic according to pattern
        @param full_name: surname name and patronymic ordered by pattern
        @return: FullName
        """
        parts = {}
        for pos, item in enumerate(full_name):
            if pos >= len(self.__positions):
                break
            parts[self.__positions[pos]] = item if item else ""

        return FullName(str(parts.get('S', '')), str(parts.get('N', '')), str(parts.get('P', '')))

    def parse_str(self, full_name: str) -> FullName:
        """
        Method for parsing string with surname name and patronymic according to pattern
        @param full_name: sting with full_name, ordered by pattern
        @return: FullName
        """
        return self.parse_list(*full_name.split())

    def parse(self, name: str | list | tuple) -> FullName:
        if name is str:
            return self.parse_str(name)

        if name is tuple or name is list:
            return self.parse_list(name)

        raise TypeError()

    def __str__(self):
        return ''.join(self.__positions)
