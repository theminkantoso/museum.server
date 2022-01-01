import re
import random
import string


class AccountService():

    @staticmethod
    def random_string():
        str1 = ''.join((random.choice(string.ascii_letters) for x in range(6)))
        str1 += ''.join((random.choice(string.digits) for x in range(6)))

        sam_list = list(str1)
        random.shuffle(sam_list)
        final_string = ''.join(sam_list)
        return final_string

    @staticmethod
    def validate_regex(in_str, in_regex):
        pattern = re.compile(in_regex)
        if pattern.fullmatch(in_str):
            return True
        return False
