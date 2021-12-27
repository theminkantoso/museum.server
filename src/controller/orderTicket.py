from datetime import datetime, date
from flask_restful import Resource, reqparse

from src.models.ticketDb import TicketDb
from src.models.orderDb import OrderDb
from src.models.ageGroupDb import AgeGroupDb

import random
import string


def random_string():
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(10)))
    str1 += ''.join((random.choice(string.digits) for x in range(10)))

    sam_list = list(str1)
    random.shuffle(sam_list)
    final_string = ''.join(sam_list)
    return final_string


class OrderTicket(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('OrderDate')
    parser.add_argument('children', type=int)
    parser.add_argument('adult', type=int)
    parser.add_argument('elderly', type=int)

    def get(self):
        return {'artifacts': list(map(lambda x: x.json(), AgeGroupDb.query.all()))}, 200

    def post(self):
        data = OrderTicket.parser.parse_args()
        order_date = data['order_date']
        children = data['children']
        adult = data['adult']
        elderly = data['elderly']
        total = data['total']
        try:
            qrcode = random_string()
            order = OrderDb(OrderDate=order_date, TotalPrice=total, CreatedAt=datetime.now(), QRCode=qrcode)
            order.save_to_db()
            order_id = OrderDb.find_by_qr(qrcode)
            children_ticket = TicketDb(OrderId=order_id.OrderId, NumberPerson=children, TicketType=1)
            adult_ticket = TicketDb(OrderId=order_id.OrderId, NumberPerson=adult, TicketType=2)
            elderly_ticket = TicketDb(OrderId=order_id.OrderId, NumberPerson=elderly, TicketType=3)
            children_ticket.save_to_db()
            adult_ticket.save_to_db()
            elderly_ticket.save_to_db()
            return {"qrcode": qrcode}, 200
        except:
            return {"msg": "Error saving your ticket"}, 400

    def delete(self):
        return {'msg': 'Not allowed'}, 404

    def put(self):
        return {'msg': 'Not allowed'}, 404


class OrderQR(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('qrcode')

    def get(self):
        data = OrderDb.parser.parse_args()
        qrcode = data['qrcode']
        qr_check = OrderDb.find_by_qr(qr=qrcode)
        today = date.today()
        if qr_check is not None:
            if today < qr_check.OrderDate:
                return {'msg': 'Not today yet'}, 200
            elif today > qr_check.OrderDate:
                qr_check.used = True
                qr_check.commit_to_db()
                return {'msg': 'Da qua ngay dat ve'}, 200
            else:
                if not qr_check.used:
                    qr_check.used = True
                    qr_check.commit_to_db()
                    return {'msg': 'success', 'order_detail': qr_check.json()}, 200
                else:
                    return {'msg': 'Ban da dung ve nay roi!'}, 200
        return {'message': 'no order matching'}, 404
