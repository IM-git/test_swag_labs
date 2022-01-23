import random
import string
from selenium.webdriver.common.keys import Keys


class RandomTools:

    # CREATED RANDOM STRING
    class String:

        @staticmethod
        def get_random_string(length):
            letters = string.ascii_lowercase
            rand_string = ''.join(
                random.choice(letters) for _ in range(length))
            return rand_string

        @staticmethod
        def generate_number():
            num = random.randint(4, 8)
            return RandomTools.String.get_random_string(num)

        @staticmethod
        def get_random_password(length=8, chars=string.ascii_letters + string.digits):
            return ''.join([random.choice(chars) for i in range(length)])

    # CREATED RANDOM STEPS
    class Steps:

        @staticmethod
        def do_random_steps(value):     # Generate random quantity steps
            random_way = random.randint(1, 2)
            if random_way == 2:
                return RandomTools.Steps.make_steps(
                    value, start=0, end=75, side=Keys.ARROW_RIGHT)
            else:
                return RandomTools.Steps.make_steps(
                    value, start=0, end=25, side=Keys.ARROW_LEFT)

        @staticmethod
        def make_steps(value, start, end, side):
            step = random.randint(start, end)
            for x in range(0, step):  # Quantity taps
                value.send_keys(side)
            return step

    class RandomValue:

        @staticmethod
        def get_random_value(initial_value, end_value):
            return random.randint(initial_value, end_value)

        @staticmethod
        def get_random_value_from_text_list(values):
            quantity = len(values) - 1
            num = random.randint(0, quantity)
            return values[num]
