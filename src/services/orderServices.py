import ast
import random
import string
import qrcode
from datetime import datetime

from src.models.orderDb import OrderDb
from src.models.accountDb import AccountDb


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

    @staticmethod
    def convert_to_dict_sou(str_arr):
        dict_out = {}
        for i in range(len(str_arr)):
            temp = str_arr[i]
            dict_temp = ast.literal_eval(temp)
            for x, y in dict_temp.items():
                dict_out[x] = y
        return dict_out

    @staticmethod
    def generate_qr(in_str):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(in_str)
        qr.make(fit=True)
        return qr

    @staticmethod
    def convert_date(date):
        try:
            out_date = datetime.strptime(date, '%Y-%m-%d').date()
            return out_date
        except:
            return ''

    @staticmethod
    def json1(order: OrderDb):
        if isinstance(order.OrderDate, datetime.date):
            order.OrderDate = order.OrderDate.strftime("%Y-%m-%d")
        if isinstance(order.CreatedAt, datetime.date):
            order.CreatedAt = order.CreatedAt.strftime("%Y-%m-%d")

        return {
            "OrderId": order.OrderId,
            "OrderDate": order.OrderDate,
            "TotalPrice": order.TotalPrice,
            "CreatedAt": order.CreatedAt
        }

    @staticmethod
    def order_req_validate(id, id_acc):
        order_check = OrderDb.find_by_id(id)
        if order_check.AccountId != id_acc:
            return False
        return True

    @staticmethod
    def get_account(email):
        return AccountDb.find_by_email(email)


