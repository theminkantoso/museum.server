from flask import jsonify
from flask_restful import Resource, reqparse
from src.models.notificationDb import Notification

class notification(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('NotificationId', type=int)
    parser.add_argument('AccountId', type=int)
    parser.add_argument('Title', type=str)
    parser.add_argument('Content', type=str)
    parser.add_argument('Time')
    parser.add_argument('Unread', type=int)

    def get(self, id):
        data = Notification.find_by_Id(id)
        if data:
            return data.json()
        return {'message': 'not found'}, 404

    def post(self):
        data = notification.parser.parse_args()
        if Notification.find_by_title(data['Title']):
            return {'message': "An notification with title '{}' already exists.".format(data['Title'])}, 400
        r = Notification(**data)
        try:
            r.save_to_db()
            return r.json(), 201
        except:
            return {"message": "error"}, 500

    def delete(self, id):
        # tim va xoa danh gia theo id cua noti
        r = Notification.find_by_Id(id)
        if r:
            r.delete_from_db()
            return {'message': 'notification: deleted.'}
        return {'message': ' not found.'}, 404

    def put(self, id):
        #  sua noti
        data = notification.parser.parse_args()
        r = Notification.find_by_Id(id)
        if r:
            r.AccountId = data['AccountId']
            r.Title = data['Title']
            r.Content = data['Content']
            r.Time = data['Time']
            r.Unread = data['Unread']
            r.save_to_db()
            return r.json()
        return {'message': 'not found.'}, 404

class Notifications(Resource):
    def get(self):
        data = {'notifications': list(map(lambda x: x.json(), Notification.query.all()))}
        return data