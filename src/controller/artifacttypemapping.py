from flask_restful import Resource, reqparse
from src.models.artifacttypemappingDb import ArtifactTypeMapping

class artifactTypeMapping(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ArtifactId', type=int)
    parser.add_argument('ArtifactTypeId', type=int)

    def get(self, id, typeId):
        atf = ArtifactTypeMapping.find_by_id1(id)
        atft = ArtifactTypeMapping.find_by_id2(typeId)
        if (atf == atft) & (not (atf is None)) :
            return atf.json()
        return {'message': 'ArtifactTypeMapping not found'}, 404

    def post(self):
        data = artifactTypeMapping.parser.parse_args()
        atf = ArtifactTypeMapping.find_by_id1(data.get('ArtifactId'))
        atft = ArtifactTypeMapping.find_by_id2(data.get('ArtifactTypeId'))
        if (atf == atft) & (not (atf is None)):
                return {'message': "An ArtifactTypeMapping already exists."}, 400
        art = ArtifactTypeMapping(**data)
        try:
            art.save_to_db()
        except:
            return {"message": "An error occurred inserting the ArtifactTypeMapping."}, 500
        return {"message": "ArtifactTypeMapping added."}, 201

    def delete(self, id, typeId):
        atf = ArtifactTypeMapping.find_by_id1(id)
        atft = ArtifactTypeMapping.find_by_id2(typeId)
        if (atf == atft) & (not (atf is None)):
            atf.delete_from_db()
            return {'message': 'Artifact deleted.'}
        return {'message': 'ArtifactTypeMapping not found'}, 404

#Hiển thị cả bảng
class artifactTypeMappings(Resource):
    def get(self):
        return {'artifactTypeMappings': list(map(lambda x: x.json(), ArtifactTypeMapping.query.all()))}

#Hiển thị theo typeId
class artifactsType(Resource):
    def get(self, id):
        return {'artifactsType': list(map(lambda x: x.json(), ArtifactTypeMapping.find_by_id(id)))}

