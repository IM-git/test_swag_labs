import random
from tools import RandomTools
from tools import DataNames


class RandomName:

    @staticmethod
    def choice_gender():
        genders = ["girls", "boys"]
        num = random.randint(0, 1)
        return genders[num]

    @staticmethod
    def random_name(way):
        get_data_names = DataNames._get_list_names(way)
        get_gender = RandomName.choice_gender()
        name = RandomTools.RandomValue.get_random_value_from_text_list(get_data_names[get_gender])
        # print(name)
        return name


class RandomUserName:

    @staticmethod
    def get_random_user_name(list_name):
        list_length = len(list_name) - 1
        num = random.randint(0, list_length)
        return list_name[num]
