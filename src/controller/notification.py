from datetime import datetime

from flask_restful import Resource, reqparse
from src.models.notificationDb import Notification


class notification(Resource):

    def get(self, AccId):
        data = Notification.find_by_AccId(AccId)
        if data:
            return data.json(), 200
        return {'message': 'not found'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('NotificationId', type=int)
        parser.add_argument('AccountId', type=int)
        parser.add_argument('Title', type=str)
        parser.add_argument('Content', type=str)
        data = parser.parse_args()
        timeNow = datetime.now()
        r = Notification(AccountId=data["AccountId"], Title=data["Title"],
                         Content=data["Content"], Time=timeNow, Unread=0)
        try:
            r.save_to_db()
            return r.json(), 201
        except Exception as e:
            print(e)
            return {"message": "error"}, 500

    def put(self, AccId):
        parser = reqparse.RequestParser()
        parser.add_argument('Unread', type=int)  # Khi người dùng đọc thông báo
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


# Thông báo Admin cho tất cả người dùng
class NotificationsAll(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Title', type=str)
    parser.add_argument('Content', type=str)
    parser.add_argument('Time')
    parser.add_argument('Unread', type=int)  # Khi người dùng đọc thông báo

    def post(self):
        data = notification.parser.parse_args()
        if data["Title"] is not None and Notification.find_by_title(data['Title']):
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
            return {'message': 'notification: deleted.'}, 200
        return {'message': ' not found.'}, 404


class Notifications(Resource):  # tất cả thông báo của mỗi người dùng.
    def get(self, AccId):
        data = {'notifications': list(map(lambda x: x.json(), Notification.query.all()))}
        return data

#  post 1 thông báo => lưu cho tất cả người dùng (Admin) => Không cần gửi id người dùng
#  người dùng đọc 1  thông báo => gửi unread.
#  Hệ thống post thông báo riêng => cho 1 người dùng =>  gửi id người dùng kèm thông báo
