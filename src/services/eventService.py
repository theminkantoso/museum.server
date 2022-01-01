import re

from src.models.museumeventDb import Museumevent

regex_id = '^[0-9]*$'


def validate_regex(input_string, regex):
    pattern = re.compile(regex)
    if pattern.fullmatch(input_string):
        return True
    return False


class EventService:

    @staticmethod
    def event_exist(id: int):
        if not validate_regex(id, regex_id):
            return 0
        evt = Museumevent.find_by_id(id)
        if evt:
            return evt.json()
        return None

    @staticmethod
    def insert_event(data: dict):
        if Museumevent.find_by_name(data.get('name')):
            return 0
        evt = Museumevent(**data)
        try:
            evt.save_to_db()
            return 1
        except:
            return None

    @staticmethod
    def delete_event(id: int):
        if not validate_regex(id, regex_id):
            return 0
        evt = Museumevent.find_by_id(id)
        if evt:
            try:
                evt.delete_from_db()
                return 1
            except:
                return 2
        return None

    @staticmethod
    def update_event(id: int, data: dict):
        if not validate_regex(id, regex_id):
            return 0
        evt = Museumevent.find_by_id(id)
        if not evt:
            return None
        else:
            try:
                evt.Name = data['Name']
                evt.Description = data['Description']
                evt.OpenTime = data['OpenTime']
                evt.CloseTime = data['CloseTime']
                evt.EventDate = data['EventDate']
                evt.save_to_db()
                return 1
            except:
                return 2

    @staticmethod
    def all_event():
        evt = {'events': list(map(lambda x: x.json(), Museumevent.query.all()))}
        return evt

