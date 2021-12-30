import re

from flask_restful import Resource, reqparse
from src.models.souvenirDb import SouvenirDb


regex_id = '^[0-9]*$'


def validate_regex(input_string, regex):
    pattern = re.compile(regex)
    if pattern.fullmatch(input_string):
        return True
    return False


class souvenir(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('SouvenirId', type=int)
    parser.add_argument('Name', type=str)
    parser.add_argument('Description', type=str)
    parser.add_argument('Price', type=int)
    parser.add_argument('Discount', type=float)
    parser.add_argument('ImageId', type=int)

    def get(self, id):
        if not validate_regex(str(id), regex_id):
            return {"message": "invalid Id "}, 400
        sou = SouvenirDb.find_by_id(id)
        if sou:
            return sou.json(), 200
        return {'message': 'Souvenir not found'}, 404

    def post(self):
        data = souvenir.parser.parse_args()
        if SouvenirDb.find_by_name(data.get('Name')):
            return {'message': "An souvenir with name '{}' already exists.".format(data.get('Name'))}, 400

        sou = SouvenirDb(**data)
        try:
            sou.save_to_db()
        except:
            return {"message": "An error occurred inserting the souvenir."}, 500
        return {"Message": "Souvenir added."}, 200

    def delete(self, id):
        if not validate_regex(str(id), regex_id):
            return {"message": "invalid Id "}, 400
        sou = SouvenirDb.find_by_id(id)
        if sou:
            try:
                sou.delete_from_db()
                return {'message': 'Souvenir deleted.'}, 200
            except:
                return {"message": "An error occurred deleting the souvenir."}, 500
        return {'message': 'Souvenir not found.'}, 404

    def put(self, id):
        if not validate_regex(str(id), regex_id):
            return {"message": "invalid Id "}, 400
        data = souvenir.parser.parse_args()
        sou = SouvenirDb.find_by_id(id)

        if sou:
            try:
                sou.Name = data['Name']
                sou.Description = data['Description']
                sou.Price = data['Price']
                sou.Discount = data['Discount']
                sou.ImageId = data['ImageId']
                sou.save_to_db()
                return {'message': 'Souvenir updated.'}, 200
            except:
                return {"message": "An error occurred updating the souvenir."}, 500
        return {'message': 'Souvenir not found.'}, 404


class souvenirs(Resource):
    def get(self):
        return {'souvenirs': list(map(lambda x: x.json(), SouvenirDb.query.all()))}, 200

