import re

from flask_restful import Resource, reqparse
from src.models.museumeventDb import Museumevent

regex_id = '^[0-9]*$'


def validate_regex(input_string, regex):
    pattern = re.compile(regex)
    if pattern.fullmatch(input_string):
        return True
    return False


class Event(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('EventId', type=int)
    parser.add_argument('Name', type=str)
    parser.add_argument('Description', type=str)
    parser.add_argument('OpenTime')
    parser.add_argument('CloseTime')
    parser.add_argument('EventDate')
    parser.add_argument('Poster', type=int)

    def get(self, id):
        if not validate_regex(id, regex_id):
            return {"message": "invalid Id "}, 400
        evt = Museumevent.find_by_id(id)
        if evt:
            return evt.json(), 200
        return {'message': 'Event not found'}, 404

    def post(self):
        data = Event.parser.parse_args()
        if Museumevent.find_by_name(data.get('name')):
            return {'message': "An event with name '{}' already exists.".format(data.get('name'))}, 400
        evt = Museumevent(**data)
        try:
            evt.save_to_db()
            return {"message": "Event added."}, 200
        except:
            return {"message": "An error occurred inserting the event."}, 500

    def delete(self, id):
        if not validate_regex(id, regex_id):
            return {"message": "invalid Id "}, 400
        evt = Museumevent.find_by_id(id)
        if evt:
            try:
                evt.delete_from_db()
                return {'message': 'Event deleted.'}, 200
            except:
                return {"message": "An error occurred deleting the event."}, 500
        return {'message': 'Event not found.'}, 404

    def put(self, id):
        if not validate_regex(id, regex_id):
            return {"message": "invalid Id "}, 400
        data = Event.parser.parse_args()
        evt = Museumevent.find_by_id(id)

        if evt:
            try:
                evt.Name = data['Name']
                evt.Description = data['Description']
                evt.OpenTime = data['OpenTime']
                evt.CloseTime = data['CloseTime']
                evt.EventDate = data['EventDate']
                evt.Poster = data['Poster']
                evt.save_to_db()
                return {'message': 'Event updated.'}, 200
            except:
                return {"message": "An error occurred updating the event."}, 500
        return {'message': 'Event not found.'}, 404


class Events(Resource):
    def get(self):
        evt = {'events': list(map(lambda x: x.json(), Museumevent.query.all()))}
        return evt, 200
