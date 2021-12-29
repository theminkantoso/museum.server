from flask_restful import Resource, reqparse
from src.models.souvenirDb import SouvenirDb


class OrderSouvenir(Resource):

    def get(self):
        return {'souvenir': list(map(lambda x: x.json(), SouvenirDb.query.all()))}, 200
