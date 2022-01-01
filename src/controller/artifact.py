from flask import request, jsonify
from flask_restful import Resource, reqparse
from src.services.artifactService import ArtifactService


class artifact(Resource):
    def get(self, id):
        atf = ArtifactService.artifact_exist(id)
        if atf == 0:
            return {"message": "invalid Id "}, 400
        elif atf == 1:
            return atf, 200
        else:
            return {'message': 'Artifact not found'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ArtifactId', type=int)
        parser.add_argument('Name', type=str)
        parser.add_argument('Description', type=str)
        parser.add_argument('Level', type=int)
        parser.add_argument('ImageId', type=int)
        data = parser.parse_args()
        atf = ArtifactService.insert_artifact(data)
        if atf == 0:
            return {'message': "An artifact with name already exists."}, 400
        elif atf ==1:
            return {"message": "An error occurred inserting the artifact."}, 500
        else:
            return {"message": "Artifact added."}, 200

    def delete(self, id):
        atf = ArtifactService.delete_artifact(id)
        if atf == 0:
            return {"message": "invalid Id "}, 400
        elif atf == 1:
            return {'message': 'Artifact deleted.'}, 200
        elif atf == 2:
            return {"message": "An error occurred deleting the artifact."}, 500
        else:
            return {'message': 'Artifact not found.'}, 404

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('Name', type=str)
        parser.add_argument('Description', type=str)
        parser.add_argument('Level', type=int)
        data = parser.parse_args()
        atf = ArtifactService.update_artifact(id, data)
        if atf == 0:
            return {"message": "invalid Id "}, 400
        elif atf == 1:
            return {'message': 'Artifact updated.'}, 200
        elif atf == 2:
            return {"message": "An error occurred updating the artifact."}, 500
        else:
            return {'message': 'Artifact not found.'}, 404


class artifacts(Resource):
    def get(self):
        atf = ArtifactService.all_artifact()
        return atf, 200
