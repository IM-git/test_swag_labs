from patterns.singleton import Singleton
import json


class ReadFile(metaclass=Singleton):

    @staticmethod
    def read_file(way):
        with open(way) as text:
            data = json.load(text)
        return data
