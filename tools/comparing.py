class Comparing:

    @staticmethod
    def comparing_lists(lists_one, lists_two):
        for name in lists_one:
            if name in lists_two:
                return True
            else:
                return False
