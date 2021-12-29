import random
import string


class OrderService():
    @staticmethod
    def convert_to_dict_ticket(arr):
        return {arr[0][1]: arr[0][0], arr[1][1]: arr[1][0], arr[2][1]: arr[2][0]}

    @staticmethod
    def convert_to_dict_souvenir(arr):
        dict_out = {}
        for i in range(len(arr)):
            dict_out[(arr[i][1])] = arr[i][0]
        return dict_out

    @staticmethod
    def random_string():
        str1 = ''.join((random.choice(string.ascii_letters) for x in range(10)))
        str1 += ''.join((random.choice(string.digits) for x in range(10)))

        sam_list = list(str1)
        random.shuffle(sam_list)
        final_string = ''.join(sam_list)
        return final_string


