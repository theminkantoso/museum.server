from flask_restful import Resource, reqparse
from src.models.artifacttypeDb import ArtifactType

class artifactType(Resource) :
    parser = reqparse.RequestParser()
    parser.add_argument('ArtifactTypeId', type=id)
    parser.add_argument('Name', type=str)

    def get(self, name):
        at = ArtifactType.find_by_name(name)
        if at:
            return at.json()
        return {'message': 'ArtifactType not found'}, 404

    def post(self):
        data = artifactType.parser.parse_args()
        if ArtifactType.find_by_name(data.get('Name')):
            return {'message': "An artifactType with name '{}' already exists.".format(data.get('Name'))}, 400

        #data.__setattr__('Name', name)

        at = ArtifactType(**data)
        try:
            at.save_to_db()
        except:
            return {"message": "An error occurred inserting the artifactType."}, 500
        return {"Message": "ArtifactType added. "}, 201

    def delete(self, name):
        at = ArtifactType.find_by_name(name)
        if at:
            at.delete_from_db()
            return {'message': 'ArtifactType deleted.'}
        return {'message': 'ArtifactType not found.'}, 404

    def put(self, name):
        data = artifactType.parser.parse_args()
        at = ArtifactType.find_by_name(name)

        if at:
            at.Name = data['Name']
            at.save_to_db()
            return at.json()
        return {'message': 'ArtifactType not found.'}, 404

class artifactTypes(Resource):
    def get(self):
        return {'artifactTypes': list(map(lambda x: x.json(), ArtifactType.query.all()))}


