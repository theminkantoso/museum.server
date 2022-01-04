from flask_restful import Resource, reqparse
from src.services.eventService import EventService
from src.core.auth import admin_required
from flask_jwt_extended import jwt_required


class Event(Resource):
    @jwt_required()
    def get(self, id):
        evt = EventService.event_exist(id)
        if evt == 0:
            return {"message": "invalid Id "}, 400
        elif evt:
            return evt, 200
        else:
            return {'message': 'Event not found'}, 404

    @jwt_required()
    @admin_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('EventId', type=int)
        parser.add_argument('Name', type=str)
        parser.add_argument('Description', type=str)
        parser.add_argument('OpenTime')
        parser.add_argument('CloseTime')
        parser.add_argument('EventDate')
        parser.add_argument('Poster', type=int)
        data = parser.parse_args()
        evt = EventService.insert_event(data)
        if evt == 0:
            return {'message': "An event with name already exists."}, 400
        elif evt == 1:
            return {"message": "Event added."}, 200
        else:
            return {"message": "An error occurred inserting the event."}, 500

    @jwt_required()
    @admin_required
    def delete(self, id):
        evt = EventService.delete_event(id)
        if evt == 0:
            return {"message": "invalid Id "}, 400
        elif evt == 1:
            return {'message': 'Event deleted.'}, 200
        elif evt == 2:
            return {"message": "An error occurred deleting the event."}, 500
        else:
            return {'message': 'Event not found.'}, 404

    @jwt_required()
    @admin_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('Name', type=str)
        parser.add_argument('Description', type=str)
        parser.add_argument('OpenTime')
        parser.add_argument('CloseTime')
        parser.add_argument('EventDate')
        data = parser.parse_args()
        evt = EventService.update_event(id, data)
        if evt == 0:
            return {"message": "invalid Id "}, 400
        elif evt == 1:
            return {'message': 'Event updated.'}, 200
        elif evt == 2:
            return {"message": "An error occurred updating the event."}, 500
        else:
            return {'message': 'Event not found.'}, 404


class Events(Resource):
    @jwt_required()
    def get(self):
        evt = EventService.all_event()
        return evt, 200
