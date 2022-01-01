from flask_restful import Resource, reqparse
from src.models.accountfavoriteartifactDb import AccountFA

class accountFA(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('AccountId', type=int)
    parser.add_argument('ArtifactId', type=int)

    def get(self, AccId, id):
        a = AccountFA.find_by_id(AccId,id)
        if a :
            return a.json(), 200
        return {'message': 'AccountFavoriteArtifact not found'}, 404

    def post(self):
        data = accountFA.parser.parse_args()
        a = AccountFA.find_by_id(data.get('AccountId'), data.get('ArtifactId'))
        if a:
                return {'message': "An AccountFavoriteArtifact already exists."}, 400
        art = AccountFA(**data)
        try:
            art.save_to_db()
        except:
            return {"message": "An error occurred inserting the AccountFavoriteArtifact."}, 500
        return {"message": "AccountFavoriteArtifact added."}, 200

    def delete(self, AccId, id):
        a = AccountFA.find_by_id(AccId, id)
        if a:
            a.delete_from_db()
            return {'message': 'AccountFavoriteArtifact deleted.'}, 200
        return {'message': 'AccountFavoriteArtifact not found'}, 404


#Hiển thị theo Account
class accountFAs(Resource):
    def get(self, AccId):
        return {'AccountFavoriteArtifacts': list(map(lambda x: x.json(), AccountFA.find_by_id1(AccId)))}, 200

