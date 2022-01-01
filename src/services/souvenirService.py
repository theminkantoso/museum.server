from src.models.souvenirDb import SouvenirDb
import re

regex_id = '^[0-9]*$'


def validate_regex(input_string, regex):
    pattern = re.compile(regex)
    if pattern.fullmatch(input_string):
        return True
    return False


class SouvenirService:

    @staticmethod
    def souvenir_exist(id: int):
        if not validate_regex(str(id), regex_id):
            return 0
        sou = SouvenirDb.find_by_id(id)
        if sou:
            return sou.json()
        return None

    @staticmethod
    def insert_souvenir(data: dict):
        if SouvenirDb.find_by_name(data.get('Name')):
            return 0
        sou = SouvenirDb(**data)
        try:
            sou.save_to_db()
        except:
            return None
        return 1

    @staticmethod
    def delete_souvenir(id: int):
        if not validate_regex(str(id), regex_id):
            return 0
        sou = SouvenirDb.find_by_id(id)
        if sou:
            try:
                sou.delete_from_db()
                return 1
            except:
                return 2
        return None

    @staticmethod
    def update_souvenir(id: int, data: dict):
        if not validate_regex(str(id), regex_id):
            return 0
        sou = SouvenirDb.find_by_id(id)
        if sou:
            try:
                sou.Name = data['Name']
                sou.Description = data['Description']
                sou.Price = data['Price']
                sou.save_to_db()
                return 1
            except:
                return 2
        return None

    @staticmethod
    def all_souvenir():
        return {'souvenirs': list(map(lambda x: x.json(), SouvenirDb.query.all()))}
