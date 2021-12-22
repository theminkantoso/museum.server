import datetime

from flask import jsonify
from flask_restful import Resource, reqparse
from src.models.museumeventDb import Museumevent

class Event(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('EventId', type=int)
    parser.add_argument('Name', type=str)
    parser.add_argument('Description', type=str)
    parser.add_argument('OpenTime')
    parser.add_argument('CloseTime')
    parser.add_argument('EventDate')
    parser.add_argument('Poster', type=int)

    def get(self, name):
        evt = Museumevent.find_by_name(name)
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


    def delete(self, name):
        evt = Museumevent.find_by_name(name)
        if evt:
            evt.delete_from_db()
            return {'message': 'Event deleted.'}, 200
        return {'message': 'Event not found.'}, 404

    def put(self, name):
        data = Event.parser.parse_args()
        evt = Museumevent.find_by_name(name)

        if evt:
            evt.Name = data['Name']
            evt.Description = data['Description']
            evt.OpenTime = data['OpenTime']
            evt.CloseTime = data['CloseTime']
            evt.EventDate = data['EventDate']
            evt.Poster = data['Poster']
            evt.save_to_db()
            return evt.json(), 200
        return {'message': 'Event not found.'}, 404

class Events(Resource):
    def get(self):
        evt = {'events': list(map(lambda x: x.json(), Museumevent.query.all()))}
        return evt, 200
