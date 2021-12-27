import re
from datetime import datetime


from src.models.accountDb import AccountDb

from flask_restful import Resource, reqparse
from src.models.notificationDb import Notification


regex_id = '^[0-9]*$'


def validate_regex(input_string, regex):
    pattern = re.compile(regex)
    if pattern.fullmatch(input_string):
        return True
    return False


class notification(Resource):

    def get(self, Id, AccId):
        if not validate_regex(str(Id), regex_id) or not validate_regex(str(AccId), regex_id):
            return {"message": "invalid Id or AccountId"}, 400
        r = Notification.find_by_AccId_NotificationId(Id, AccId)
        if r:
            r.json(), 200
        return {'message': ' not found.'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('AccountId', type=int)
        parser.add_argument('Title', type=str)
        parser.add_argument('Content', type=str)
        data = parser.parse_args()
        if not validate_regex(str(data["AccountId"]), regex_id):
            return {"message": "invalid AccountId"}, 400
        timeNow = datetime.now()
        r = Notification(AccountId=data["AccountId"], Title=data["Title"],
                         Content=data["Content"], Time=timeNow, Unread=0)
        try:
            r.save_to_db()
            return r.json(), 200
        except:
            return {"message": "error"}, 500

    def put(self, Id,  AccId):
        if not validate_regex(str(Id), regex_id) or not validate_regex(str(AccId), regex_id):
            return {"message": "invalid Id or AccountId"}, 400
        parser = reqparse.RequestParser()
        parser.add_argument('Unread', type=int)  # Khi người dùng đọc thông báo
        data = parser.parse_args()
        if not data['Unread']:
            return {"message": "can't update"}, 400

        r = Notification.find_by_AccId_NotificationId(Id, AccId)
        if r:
            r.Unread = data['Unread']
            r.save_to_db()
            return r.json(), 200
        return {'message': 'not found.'}, 404

    def delete(self, Id, AccId):
        if not validate_regex(str(Id), regex_id) or not validate_regex(str(AccId), regex_id):
            return {"message": "invalid Id or AccountId"}, 400
        r = Notification.find_by_AccId_NotificationId(Id, AccId)
        if r:
            r.delete_from_db()
            return {'message': 'notification deleted.'}, 200
        return {'message': ' not found.'}, 404


# Thông báo Admin cho tất cả người dùng
class NotificationsAll(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Title', type=str)
    parser.add_argument('Content', type=str)

    def post(self):
        data = NotificationsAll.parser.parse_args()
        accounts = AccountDb.all_accounts()
        timeNow = datetime.now()
        for acc in accounts:
            r = Notification(AccountId=acc.AccountId, Title=data["Title"],
                             Content=data["Content"], Time=timeNow, Unread=0)
            try:
                r.save_to_db()
            except Exception as e:
                print(e)
                return {"message": "error"}, 500
        return {"message": "added"}, 200


class Notifications(Resource):  # tất cả thông báo của mỗi người dùng.
    def get(self, AccId):
        if not validate_regex(AccId, regex_id):
            return {"message": "invalid AccountId"}, 400
        data = {'notifications': list(map(lambda x: x.json(), Notification.find_All_Notifications_by_AccId(AccId)))}
        return data,200

#  post 1 thông báo => lưu cho tất cả người dùng (Admin) => Không cần gửi id người dùng
#  người dùng đọc 1  thông báo => gửi unread.
#  Hệ thống post thông báo riêng => cho 1 người dùng =>  gửi id người dùng kèm thông báo
