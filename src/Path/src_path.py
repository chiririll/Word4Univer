import os
from os import path

src_path = path.join(path.dirname(path.realpath(__file__)), "../src")
working_dir = os.getcwd()


def __get_path(base: str, rel_path: str = None):
    if rel_path is None:
        return base

    parts = [i for i in rel_path.split('/') if i]
    return path.join(base, *parts)


def get_src(rel_path: str = None) -> str:
    """ Function for getting absolute path to file or folder in src directory """
    return __get_path(src_path, rel_path)


def get_wd(rel_path: str = None) -> str:
    """ Function for getting absolute path to file or folder in working directory """
    return __get_path(working_dir, rel_path)
