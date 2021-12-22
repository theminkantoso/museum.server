from datetime import datetime
from flask_restful import Resource, reqparse

from src.models.ticketDb import Ticket
from src.models.orderDb import Order

import random
import string

def random_string():
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(10)))
    str1 += ''.join((random.choice(string.digits) for x in range(10)))

    sam_list = list(str1)
    random.shuffle(sam_list)
    final_string = ''.join(sam_list)
    return final_string


class Order(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('OrderDate')
    parser.add_argument('children', type=int)
    parser.add_argument('adult', type=int)
    parser.add_argument('elderly', type=int)

    def get(self):
        pass

    def post(self, id):
        data = Order.parser.parse_args()
        orderDate = data['OrderDate']
        children = data['children']
        adult = data['adult']
        elderly = data['elderly']
        try:
            qrcode= random_string()
            order = Order(OrderDate=orderDate, CreatedAt=datetime.now(), QRCode=qrcode)
            order.save_to_db()
            childrenTicket = Ticket(OrderId=order.OrderId, NumberPerson=children, TicketType=0)
            adultTicket = Ticket(OrderId=order.OrderId, NumberPerson=adult, TicketType=1)
            elderlyTicket = Ticket(OrderId=order.OrderId, NumberPerson=elderly, TicketType=2)
            childrenTicket.save_to_db()
            adultTicket.save_to_db()
            elderlyTicket.save_to_db()
            return {"qrcode": qrcode}, 200
        except:
            return {"message": "Error saving your ticket"}, 400

    def delete(self):
        return {'message': 'Not allowed'}, 404

    def put(self):
        return {'message': 'Not allowed'}, 404


class OrderQR(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('qrcode')

    def get(self):
        data = Order.parser.parse_args()
        qrcode = data['qrcode']
        qrCheck = Order.find_by_qr(qr=qrcode)
        if qrCheck is not None:
            if not qrCheck.used:
                qrCheck.used = False
                qrCheck.commit_to_db()
                return {'orderId': qrCheck.OrderId}, 200
        return {'message': 'no order matching'}, 404