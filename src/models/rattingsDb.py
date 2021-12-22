from sqlalchemy.orm import relationship

from src.database import db


class Ratting(db.Model):
    __tablename__ = 'rattings'
    RattingId = db.Column(db.Integer, primary_key=True)
    Star = db.Column(db.Float)
    Description = db.Column(db.String(500))
    AccountId = db.Column(db.Integer, db.ForeignKey('account.AccountId'))

    def __init__(self, RattingId, Star, Description, AccountId):
        self.RattingId = RattingId
        self.Star = Star
        self.Description = Description
        self.AccountId = AccountId

    def json(self):
        return {"RattingId": self.RattingId, "Star": self.Star, "Description": self.Description, "AccountId": self.AccountId}

    @classmethod
    def find_by_AccountId(cls, id):
        return cls.query.filter_by(AccountId=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()