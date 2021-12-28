import re

from flask import request, jsonify
from flask_restful import Resource, reqparse
from src.models.artifactDb import Artifact

regex_id = '^[0-9]*$'


def validate_regex(input_string, regex):
    pattern = re.compile(regex)
    if pattern.fullmatch(input_string):
        return True
    return False


class artifact(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ArtifactId', type=int)
    parser.add_argument('Name', type=str)
    parser.add_argument('Description', type=str)
    parser.add_argument('Level', type=int)
    parser.add_argument('ImageId', type=int)

    def get(self, id):
        if not validate_regex(id, regex_id):
            return {"message": "invalid Id "}, 400
        atf = Artifact.find_by_id(id)
        if atf:
            return atf.json(), 200
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
        return {"message": "Artifact added."}, 200

    def delete(self, id):
        if not validate_regex(id, regex_id):
            return {"message": "invalid Id "}, 400
        art = Artifact.find_by_id(id)
        if art:
            try:
                art.delete_from_db()
                return {'message': 'Artifact deleted.'}, 200
            except:
                return {"message": "An error occurred deleting the artifact."}, 500
        return {'message': 'Artifact not found.'}, 404

    def put(self, id):
        if not validate_regex(id, regex_id):
            return {"message": "invalid Id "}, 400
        data = artifact.parser.parse_args()
        art = Artifact.find_by_id(id)

        if art:
            try:
                art.Name = data['Name']
                art.Description = data['Description']
                art.Level = data['Level']
                art.ImageId = data['ImageId']
                art.save_to_db()
                return {'message': 'Artifact updated.'}, 200
            except:
                return {"message": "An error occurred updating the artifact."}, 500
        return {'message': 'Artifact not found.'}, 404


class artifacts(Resource):
    def get(self):
        return {'artifacts': list(map(lambda x: x.json(), Artifact.query.all()))}
