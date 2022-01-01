from datetime import datetime

from src.models.notificationDb import Notification
from src.models.accountDb import AccountDb
import re

regex_id = '^[0-9]*$'


def validate_regex(input_string, regex):
    pattern = re.compile(regex)
    if pattern.fullmatch(input_string):
        return True
    return False


class NotificationService:

    @staticmethod
    def notification_exist(id: int):
        if not validate_regex(str(id), regex_id):
            return 0
        noti = Notification.find_by_Id(id)
        if noti:
            return noti.json()
        return None

    @staticmethod
    def insert_notification(email_acc: str, data: dict):
        id_acc = AccountDb.find_by_email(email_acc).AccountId
        if not validate_regex(str(id_acc), regex_id):
            return 0
        timeNow = datetime.now()
        r = Notification(AccountId=id_acc, Title=data["Title"],
                         Content=data["Content"], Time=timeNow, Unread=0)
        try:
            r.save_to_db()
            return 1
        except:
            return 2

    @staticmethod
    def update_notification(id: int, data: dict):
        if not validate_regex(str(id), regex_id):
            return 0
        if not data['Unread']:
            return 1
        r = Notification.find_by_Id(id)
        if r:
            try:
                r.Unread = data['Unread']
                r.save_to_db()
                return 2
            except:
                return 3
        return None

    @staticmethod
    def delete_notification(id: int):
        if not validate_regex(str(id), regex_id):
            return 0
        r = Notification.find_by_Id(id)
        if r:
            try:
                r.delete_from_db()
                return 1
            except:
                return 2
        return None

    @staticmethod
    def add_notification_all(data: dict):
        accounts = AccountDb.all_accounts()
        timeNow = datetime.now()
        for acc in accounts:
            if acc.RoleId != 0:
                r = Notification(AccountId=acc.AccountId, Title=data["Title"],
                                 Content=data["Content"], Time=timeNow, Unread=0)
                try:
                    r.save_to_db()
                except:
                    return None
        return 1

    @staticmethod
    def all_notification(email_acc: str):
        id_acc = AccountDb.find_by_email(email_acc).AccountId
        data = {'notifications': list(map(lambda x: x.json(), Notification.find_All_Notifications_by_AccId(id_acc)))}
        return data
