import random


class RandomName:

    @staticmethod
    def get_random_name(list_name):
        list_length = len(list_name) - 1
        num = random.randint(0, list_length)
        return list_name[num]
