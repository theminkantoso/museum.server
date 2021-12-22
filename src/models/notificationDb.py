import datetime

from sqlalchemy.orm import relationship

from src.database import db

class Notification(db.Model):
    __tablename__ = 'notification'
    NotificationId = db.Column(db.Integer, primary_key=True)
    AccountId = db.Column(db.Integer, db.ForeignKey('account.AccountId'))
    Title = db.Column(db.String(50))
    Content = db.Column(db.String(200))
    Time = db.Column(db.Date)
    Unread = db.Column(db.Integer)


    def __init__(self, NotificationId, AccountId, Title,Content, Time, Unread ):
        self.NotificationId = NotificationId
        self.AccountId = AccountId
        self.Title = Title
        self.Content = Content
        self.Time = Time
        self.Unread = Unread

    def json(self):
        if isinstance(self.Time, datetime.date):
            self.Time = self.Time.strftime("%Y-%m-%d")
        return {"NotificationId" : self.NotificationId, "AccountId": self.AccountId,
                "Title":self.Title ,"Content": self.Content, "Time": self.Time, "Unread": self.Unread}

    @classmethod
    def find_by_Id(cls, id):
        return cls.query.filter_by(NotificationId=id).first()

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(Title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
