from datetime import date
from flask_restful import Resource, reqparse
from io import BytesIO
from flask import send_file
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from src.models.ticketDb import TicketDb
from src.models.orderDb import OrderDb
from src.models.souvenirDb import SouvenirDb
from src.models.accountDb import AccountDb
from src.services.orderServices import OrderService

import random
import string
import qrcode


class OrderSouvenir(Resource):

    def get(self):
        return {'souvenir': list(map(lambda x: x.json(), SouvenirDb.query.all()))}, 200

    def post(self):
        pass


class SouvenirOrders(Resource):

    @jwt_required()
    def get(self):
        email = get_jwt_identity()
        account = AccountDb.find_by_email(email)
        orders = OrderDb.find_by_account_order(account.AccountId)
        return {'orders': list(map(lambda x: x.json(), orders))}, 200


class SouvenirOrdersId(Resource):

    @jwt_required()
    def get(self, id):
        try:
            return send_file('./statics/images/qr_code_ticket/qr' + str(id) + '.jpeg', mimetype='image/jpeg',
                             as_attachment=True, download_name=OrderService.random_string() + '.jpeg')
        except Exception as e:
            print(e)
            return {"msg": "error"}, 404