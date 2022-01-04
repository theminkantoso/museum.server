from flask_jwt_extended import get_jwt_identity, jwt_required
from src.core.auth import admin_required

from flask_restful import Resource, reqparse
from src.services.notificationServices import NotificationService


class notification(Resource):
    @jwt_required()
    def get(self, Id):
        noti = NotificationService.notification_exist(Id)
        if noti == 0:
            return {"message": "invalid Id "}, 400
        if noti:
            return noti, 200
        return {'message': ' not found.'}, 404

    @jwt_required()
    def post(self):
        email_acc = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument('Title', type=str)
        parser.add_argument('Content', type=str)
        data = parser.parse_args()
        noti = NotificationService.insert_notification(email_acc, data)

        if noti == 0:
            return {"message": "invalid AccountId"}, 400
        elif noti == 1:
            return {"message": "Notification added."}, 200
        else:
            return {"message": "An error occurred inserting the notification."}, 500

    @jwt_required()
    def put(self, Id):
        parser = reqparse.RequestParser()
        parser.add_argument('Unread', type=int)  # Khi người dùng đọc thông báo
        data = parser.parse_args()
        noti = NotificationService.update_notification(Id, data)
        if noti == 0:
            return {"message": "invalid Id"}, 400
        elif noti == 1:
            return {"message": "can't update"}, 400
        elif noti == 2:
            return {"message": "Notification updated."}, 200
        elif noti == 3:
            return {"message": "An error occurred updating the notification."}, 500
        else:
            return {'message': 'not found.'}, 404

    @jwt_required()
    def delete(self, Id):
        noti = NotificationService.delete_notification(Id)
        if noti == 0:
            return {"message": "invalid Id"}, 400
        elif noti == 1:
            return {'message': 'notification deleted.'}, 200
        elif noti == 2:
            return {"message": "An error occurred deleting the notification."}, 500
        else:
            return {'message': 'Notification not found.'}, 404


# Thông báo Admin cho tất cả người dùng
class NotificationsAll(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Title', type=str)
    parser.add_argument('Content', type=str)

    @jwt_required()
    @admin_required
    def post(self):
        data = NotificationsAll.parser.parse_args()
        noti = NotificationService.add_notification_all(data)
        if noti == 1:
            return {"message": "Notification added"}, 200
        else:
            return {"message": "An error occurred inserting the notification."}, 500


class Notifications(Resource):  # tất cả thông báo của mỗi người dùng.
    @jwt_required()
    def get(self):
        email_acc = get_jwt_identity()
        noti = NotificationService.all_notification(email_acc)
        return noti, 200

#  post 1 thông báo => lưu cho tất cả người dùng (Admin) => Không cần gửi id người dùng
#  người dùng đọc 1  thông báo => gửi unread.
#  Hệ thống post thông báo riêng => cho 1 người dùng =>  gửi id người dùng kèm thông báo
