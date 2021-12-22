from flask import request, jsonify
from flask_restful import Resource, reqparse
from src.models.artifactDb import Artifact

class artifact(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ArtifactId', type=int)
    parser.add_argument('Name', type=str)
    parser.add_argument('Description', type=str)
    parser.add_argument('Level', type=int)
    parser.add_argument('ImageId', type=int)

    def get(self, name):
        atf = Artifact.find_by_name(name)
        if atf:
            return atf.json()
        return {'message': 'Artifact not found'}, 404

    def post(self):
        data = artifact.parser.parse_args()
        if Artifact.find_by_name(data.get('Name')):
            return {'message': "An artifact with name '{}' already exists.".format(data.get('Name'))}, 400
        art = Artifact(**data)
        try:
            art.save_to_db()
        except:
            return {"message": "An error occurred inserting the artifact."}, 500
        return {"message": "Artifact added."}, 201

    def delete(self, name):
        art = Artifact.find_by_name(name)
        if art:
            art.delete_from_db()
            return {'message': 'Artifact deleted.'}
        return {'message': 'Artifact not found.'}, 404

    def put(self, name):
        data = artifact.parser.parse_args()
        art = Artifact.find_by_name(name)

        if art:
            art.Name = data['Name']
            art.Description = data['Description']
            art.Level = data['Level']
            art.ImageId = data['ImageId']
            art.save_to_db()
            return art.json()
        return {'message': 'Artifact not found.'}, 404

class artifacts(Resource):
    def get(self):
        return {'artifacts': list(map(lambda x: x.json(), Artifact.query.all()))}

