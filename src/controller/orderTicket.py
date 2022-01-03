from datetime import date, datetime
from flask_restful import Resource, reqparse
from io import BytesIO
from flask import send_file
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from src.models.ticketDb import TicketDb
from src.models.orderDb import OrderDb
from src.models.ageGroupDb import AgeGroupDb
from src.models.accountDb import AccountDb
from src.services.orderServices import OrderService


def json1(order):
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


class OrderTicket(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('order_date')
    parser.add_argument('children', type=int)
    parser.add_argument('adult', type=int)
    parser.add_argument('elderly', type=int)
    parser.add_argument('total', type=int)

    def get(self):
        return {'artifacts': list(map(lambda x: x.json(), AgeGroupDb.query.all()))}, 200

    @jwt_required()
    def post(self):
        email = get_jwt_identity()
        account = AccountDb.find_by_email(email)
        data = OrderTicket.parser.parse_args()
        order_date = data['order_date']
        children = data['children']
        adult = data['adult']
        elderly = data['elderly']
        total = data['total']
        try:
            # order_date = OrderService.convert_date(order_date)
            # if order_date == '':
            #     return {'msg': 'Invalid input'}, 400
            qrcode_str = OrderService.random_string()

            # prevent duplicate
            order_check_dup = OrderDb.find_by_qr(qrcode_str)
            while order_check_dup is not None:
                qrcode_str = OrderService.random_string()
                order_check_dup = OrderDb.find_by_qr(qrcode_str)

            order = OrderDb(OrderDate=order_date, TotalPrice=total, CreatedAt=date.today(), AccountId=account.AccountId,
                            QRCode=qrcode_str, type=0)
            order.save_to_db()
            order_id = OrderDb.find_by_qr(qrcode_str)
            children_ticket = TicketDb(OrderId=order_id.OrderId, NumberPerson=children, TicketType=1)
            adult_ticket = TicketDb(OrderId=order_id.OrderId, NumberPerson=adult, TicketType=2)
            elderly_ticket = TicketDb(OrderId=order_id.OrderId, NumberPerson=elderly, TicketType=3)
            children_ticket.save_to_db()
            adult_ticket.save_to_db()
            elderly_ticket.save_to_db()

            qr = OrderService.generate_qr(qrcode_str)
            img = qr.make_image(fill_color="black", back_color="white")

            buffer = BytesIO()
            img.get_image().save(buffer, 'JPEG', quality=70)
            buffer.seek(0)
            img.save('./statics/images/qr_code_ticket/qr'+str(order_id.OrderId)+'.jpeg')
            # return send_file(buffer, mimetype='image/jpeg', as_attachment=True, download_name=random_string()+'.jpeg')
            # return send_file('./statics/images/qr_code_ticket/qr' + str(order_id.OrderId) +'.jpeg',
            #                  mimetype='image/jpeg', as_attachment=True,
            #                  download_name=OrderService.random_string()+'.jpeg')
            return {"urlImage": 'statics/images/qr_code_ticket/qr' + str(order_id.OrderId) + '.jpeg'}
        except Exception as e:
            print(e)
            return {"msg": "Error saving your ticket"}, 400

    def delete(self):
        return {'msg': 'Not allowed'}, 404

    def put(self):
        return {'msg': 'Not allowed'}, 404


class OrderQR(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('qrcode')

    def post(self):
        data = OrderQR.parser.parse_args()
        qrcode = data['qrcode']
        qr_check = OrderDb.find_by_qr(qr=qrcode)
        today = date.today()
        if qr_check is not None:
            if today < qr_check.OrderDate:
                return {'msg': 'Chưa đến ngày trên vé', 'order_date': qr_check.OrderDate.isoformat()}, 200
            elif today > qr_check.OrderDate:
                qr_check.used = True
                qr_check.commit_to_db()
                return {'msg': 'Đã quá ngày trên vé', 'order_date': qr_check.OrderDate.isoformat()}, 200
            else:
                if not qr_check.used:
                    qr_check.used = True
                    qr_check.commit_to_db()
                    if qr_check.type == 0:
                        order_detail = OrderDb.qr_detail_ticket(qrcode)
                        return {'msg': 'success', 'order_date': qr_check.OrderDate.isoformat(),
                                'order_detail': OrderService.convert_to_dict_ticket(order_detail)}, 200
                    elif qr_check.type == 1:
                        order_detail = OrderDb.qr_detail_order_sou(qrcode)
                        return {'msg': 'success', 'order_date': qr_check.OrderDate.isoformat(),
                                'order_detail': OrderService.convert_to_dict_souvenir(order_detail)}, 200
                else:
                    return {'msg': 'Bạn đã dùng vé này rồi!'}, 200
        return {'message': 'Không có đơn đặt nào được tìm thấy'}, 404


class TicketOrders(Resource):

    @jwt_required()
    def get(self):
        email = get_jwt_identity()
        account = AccountDb.find_by_email(email)
        orders = OrderDb.find_by_account_ticket(account.AccountId)
        # return {'orders': list(map(lambda x: x.json(), orders))}, 200
        return {'orders': list(map(lambda x: json1(x), orders))}, 200


class TicketOrdersId(Resource):

    @jwt_required()
    def get(self, id):
        try:
            # return send_file('./statics/images/qr_code_ticket/qr' + str(id) + '.jpeg', mimetype='image/jpeg',
            #                  as_attachment=True, download_name=OrderService.random_string() + '.jpeg')
            return {"urlImage": 'statics/images/qr_code_ticket/qr' + str(id) + '.jpeg'}
        except Exception as e:
            print(e)
            return {"msg": "error"}, 404




