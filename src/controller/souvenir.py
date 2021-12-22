from flask_restful import Resource, reqparse
from src.models.souvenirDb import Souvenir

class souvenir(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('SouvenirId', type=int)
    parser.add_argument('Name', type=str)
    parser.add_argument('Description', type=str)
    parser.add_argument('Price', type=int)
    parser.add_argument('Discount', type=float)
    parser.add_argument('ImageId', type=int)

    def get(self, name):
        sou = Souvenir.find_by_name(name)
        if sou:
            return sou.json()
        return {'message': 'Souvenir not found'}, 404

    def post(self):
        data = souvenir.parser.parse_args()
        if Souvenir.find_by_name(data.get('Name')):
            return {'message': "An souvenir with name '{}' already exists.".format(data.get('Name'))}, 400

        sou = Souvenir(**data)
        try:
            sou.save_to_db()
        except:
            return {"message": "An error occurred inserting the souvenir."}, 500
        return {"Message": "Souvenir added. "}, 201

    def delete(self, name):
        sou = Souvenir.find_by_name(name)
        if sou:
            sou.delete_from_db()
            return {'message': 'Souvenir deleted.'}
        return {'message': 'Souvenir not found.'}, 404

    def put(self, name):
        data = souvenir.parser.parse_args()
        sou = Souvenir.find_by_name(name)

        if sou:
            sou.Name = data['Name']
            sou.Description = data['Description']
            sou.Price = data['Price']
            sou.Discount = data['Discount']
            sou.ImageId = data['ImageId']
            sou.save_to_db()
            return sou.json()
        return {'message': 'Souvenir not found.'}, 404

class souvenirs(Resource):
    def get(self):
        return {'souvenirs': list(map(lambda x: x.json(), Souvenir.query.all()))}

