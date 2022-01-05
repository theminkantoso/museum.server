from datetime import date
from flask_restful import Resource, reqparse
from io import BytesIO
from flask import send_file
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.models.orders_souvenirDb import OrderSouvernirDetailDb
from src.models.orderDb import OrderDb
from src.models.souvenirDb import SouvenirDb
from src.models.accountDb import AccountDb
from src.services.orderServices import OrderService


def json1(order):
    if isinstance(order.OrderDate, date):
        order.OrderDate = order.OrderDate.strftime("%Y-%m-%d")
    if isinstance(order.CreatedAt, date):
        order.CreatedAt = order.CreatedAt.strftime("%Y-%m-%d")

    return {
        "OrderId": order.OrderId,
        "OrderDate": order.OrderDate,
        "TotalPrice": order.TotalPrice,
        "CreatedAt": order.CreatedAt
    }


class OrderSouvenir(Resource):

    def get(self):
        return {'souvenir': list(map(lambda x: x.json(), SouvenirDb.query.all()))}, 200

    @jwt_required()
    def post(self):
        email = get_jwt_identity()
        account = AccountDb.find_by_email(email)
        parser = reqparse.RequestParser()
        parser.add_argument('orders', action='append')
        parser.add_argument('order_date')
        data = parser.parse_args()
        in_arr = data['orders']
        order_date = data['order_date']
        dict_in = OrderService.convert_to_dict_sou(in_arr)
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

            order = OrderDb(OrderDate=order_date, TotalPrice=0, CreatedAt=date.today(), AccountId=account.AccountId,
                            QRCode=qrcode_str, type=1)
            order.save_to_db()
            order_id = OrderDb.find_by_qr(qrcode_str)
            for x, y in dict_in.items():
                order_sou_models = OrderSouvernirDetailDb(orderId=order_id.OrderId, souvernirId=int(x), quantity=y)
                order_sou_models.save_to_db()

            qr = OrderService.generate_qr(qrcode_str)
            img = qr.make_image(fill_color="black", back_color="white")

            buffer = BytesIO()
            img.get_image().save(buffer, 'JPEG', quality=70)
            buffer.seek(0)
            img.save('./statics/images/qr_code_order/qr' + str(order_id.OrderId) + '.jpeg')
            # return send_file('./statics/images/qr_code_order/qr' + str(order_id.OrderId) + '.jpeg',
            #                  mimetype='image/jpeg', as_attachment=True,
            #                  download_name=OrderService.random_string() + '.jpeg')
            return {"urlImage": 'statics/images/qr_code_order/qr' + str(order_id.OrderId) + '.jpeg'}
        except Exception as e:
            print(e)
            return {"msg": "Error saving your order"}, 400


class SouvenirOrders(Resource):

    @jwt_required()
    def get(self):
        email = get_jwt_identity()
        account = AccountDb.find_by_email(email)
        orders = OrderDb.find_by_account_order(account.AccountId)
        # return {'orders': list(map(lambda x: x.json(), orders))}, 200
        return {'orders': list(map(lambda x: x.json1(), orders))}, 200


class SouvenirOrdersId(Resource):

    @jwt_required()
    def get(self, id):
        email_acc = get_jwt_identity()
        account_now = OrderService.get_account(email_acc)
        if not OrderService.order_req_validate(id, account_now.AccountId):
            return {'msg': 'not authorized'}, 403
        try:
            # return send_file('./statics/images/qr_code_order/qr' + str(id) + '.jpeg', mimetype='image/jpeg',
            #                  as_attachment=True, download_name=OrderService.random_string() + '.jpeg')
            return {"urlImage": 'statics/images/qr_code_order/qr' + str(id) + '.jpeg'}
        except Exception as e:
            print(e)
            return {"msg": "error"}, 404