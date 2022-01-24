from patterns.singleton import Singleton
from tools import ReadFile
import json

WAY = 'tools/data_names.json'


class DataNames(metaclass=Singleton):

    @staticmethod
    def _get_list_names(path):
        return ReadFile.read_file(path)
