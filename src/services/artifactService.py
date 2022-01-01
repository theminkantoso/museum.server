import re
from src.models.artifactDb import Artifact


regex_id = '^[0-9]*$'


def validate_regex(input_string, regex):
    pattern = re.compile(regex)
    if pattern.fullmatch(input_string):
        return True
    return False


class ArtifactService:
    @staticmethod
    def artifact_exist(id: int):
        if not validate_regex(str(id), regex_id):
            return 0
        atf = Artifact.find_by_id(id)
        if atf:
            return atf.json()
        return None

    @staticmethod
    def insert_artifact(data: dict):
        if Artifact.find_by_name(data.get('Name')):
            return 0
        art = Artifact(**data)
        try:
            art.save_to_db()
        except:
            return 1
        return 2

    @staticmethod
    def delete_artifact(id: int):
        if not validate_regex(str(id), regex_id):
            return 0
        art = Artifact.find_by_id(id)
        if art:
            try:
                art.delete_from_db()
                return 1
            except:
                return 2
        return None

    @staticmethod
    def update_artifact(id: int, data: dict):
        if not validate_regex(str(id), regex_id):
            return 0
        art = Artifact.find_by_id(id)
        if art:
            try:
                art.Name = data['Name']
                art.Description = data['Description']
                art.Level = data['Level']
                art.save_to_db()
                return 1
            except:
                return 2
        return None

    @staticmethod
    def all_artifact():
        return {'artifacts': list(map(lambda x: x.json(), Artifact.query.all()))}