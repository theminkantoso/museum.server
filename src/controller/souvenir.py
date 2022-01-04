from src.services.souvenirService import SouvenirService
from flask_restful import Resource, reqparse
from src.core.auth import admin_required
from flask_jwt_extended import jwt_required


class souvenir(Resource):
    @jwt_required()
    def get(self, id):
        sou = SouvenirService.souvenir_exist(id)
        if sou == 0:
            return {"message": "invalid Id "}, 400
        elif sou:
            return sou, 200
        return {'message': 'Souvenir not found'}, 404

    @jwt_required()
    @admin_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('SouvenirId', type=int)
        parser.add_argument('Name', type=str)
        parser.add_argument('Description', type=str)
        parser.add_argument('Price', type=int)
        parser.add_argument('ImageId', type=int)
        data = parser.parse_args()
        sou = SouvenirService.insert_souvenir(data)
        if sou == 0:
            return {'message': "An souvenir with name already exists."}, 400
        elif sou == 1:
            return {"Message": "Souvenir added."}, 200
        else:
            return {"message": "An error occurred inserting the souvenir."}, 500

    @jwt_required()
    @admin_required
    def delete(self, id):
        sou = SouvenirService.delete_souvenir(id)
        if sou == 0:
            return {"message": "invalid Id "}, 400
        elif sou == 1:
            return {'message': 'Souvenir deleted.'}, 200
        elif sou == 2:
            return {"message": "An error occurred deleting the souvenir."}, 500
        else:
            return {'message': 'Souvenir not found.'}, 404

    @jwt_required()
    @admin_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('Name', type=str)
        parser.add_argument('Description', type=str)
        parser.add_argument('Price', type=int)
        data = parser.parse_args()
        sou = SouvenirService.update_souvenir(id, data)
        if sou == 0:
            return {"message": "invalid I"}, 400
        elif sou == 1:
            return {'message': 'Souvenir updated.'}, 200
        elif sou == 2:
            return {"message": "An error occurred updating the souvenir."}, 500
        else:
            return {'message': 'Souvenir not found.'}, 404


class souvenirs(Resource):
    @jwt_required()
    def get(self):
        sou = SouvenirService.all_souvenir()
        return sou, 200

