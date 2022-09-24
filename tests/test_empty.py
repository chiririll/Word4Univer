import src


class TestLab(src.Lab):
    def __init__(self, **params):
        super().__init__(src.LabInfo(), src.StudentInfo(), **params)

    def add_input(self, key: str, value) -> None:
        pass

    def run(self):
        pass


def main():
    lab = TestLab()
    lab.run()
    lab.save_to_file()


if __name__ == "__main__":
    main()
