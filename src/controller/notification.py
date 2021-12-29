import re
from datetime import datetime
from flask_jwt_extended import get_jwt_identity, jwt_required

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
    @jwt_required()
    def get(self, Id):
        if not validate_regex(str(Id), regex_id):
            return {"message": "invalid Id "}, 400
        r = Notification.find_by_Id(Id)
        if r:
            return r.json(), 200
        return {'message': ' not found.'}, 404

    @jwt_required()
    def post(self):
        email_acc = get_jwt_identity()
        id_acc = AccountDb.find_by_email(email_acc).AccountId
        parser = reqparse.RequestParser()
        parser.add_argument('Title', type=str)
        parser.add_argument('Content', type=str)
        data = parser.parse_args()
        print(data)
        if not validate_regex(str(id_acc), regex_id):
            return {"message": "invalid AccountId"}, 400
        timeNow = datetime.now()
        r = Notification(AccountId=id_acc, Title=data["Title"],
                         Content=data["Content"], Time=timeNow, Unread=0)
        try:
            r.save_to_db()
            return {"message": "Notification added."}, 200
        except:
            return {"message": "An error occurred inserting the notification."}, 500

    @jwt_required()
    def put(self, Id):
        if not validate_regex(str(Id), regex_id):
            return {"message": "invalid Id"}, 400
        parser = reqparse.RequestParser()
        parser.add_argument('Unread', type=int)  # Khi người dùng đọc thông báo
        data = parser.parse_args()
        if not data['Unread']:
            return {"message": "can't update"}, 400

        r = Notification.find_by_Id(Id)
        if r:
            try:
                r.Unread = data['Unread']
                r.save_to_db()
                return {"message": "Notification updated."}, 200
            except:
                return {"message": "An error occurred updating the notification."}, 500
        return {'message': 'not found.'}, 404

    @jwt_required()
    def delete(self, Id):
        if not validate_regex(str(Id), regex_id):
            return {"message": "invalid Id"}, 400
        r = Notification.find_by_Id(Id)
        if r:
            try:
                r.delete_from_db()
                return {'message': 'notification deleted.'}, 200
            except:
                return {"message": "An error occurred deleting the notification."}, 500
        return {'message': 'Notification not found.'}, 404


# Thông báo Admin cho tất cả người dùng
class NotificationsAll(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Title', type=str)
    parser.add_argument('Content', type=str)

    @jwt_required()
    def post(self):
        data = NotificationsAll.parser.parse_args()
        accounts = AccountDb.all_accounts()
        timeNow = datetime.now()
        for acc in accounts:
            if acc.RoleId != 0:
                r = Notification(AccountId=acc.AccountId, Title=data["Title"],
                                 Content=data["Content"], Time=timeNow, Unread=0)
                try:
                    r.save_to_db()
                except:
                    return {"message": "An error occurred inserting the notification."}, 500
        return {"message": "Notification added"}, 200


class Notifications(Resource):  # tất cả thông báo của mỗi người dùng.
    @jwt_required()
    def get(self):
        email_acc = get_jwt_identity()
        id_acc = AccountDb.find_by_email(email_acc).AccountId
        if not validate_regex(str(id_acc), regex_id):
            return {"message": "invalid AccountId"}, 400
        data = {'notifications': list(map(lambda x: x.json(), Notification.find_All_Notifications_by_AccId(id_acc)))}
        return data, 200

#  post 1 thông báo => lưu cho tất cả người dùng (Admin) => Không cần gửi id người dùng
#  người dùng đọc 1  thông báo => gửi unread.
#  Hệ thống post thông báo riêng => cho 1 người dùng =>  gửi id người dùng kèm thông báo
