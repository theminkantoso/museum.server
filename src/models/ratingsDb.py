from src.database import db


class Rating(db.Model):
    __tablename__ = 'ratings'
    RatingId = db.Column(db.Integer, primary_key=True)
    Star = db.Column(db.Integer)
    Description = db.Column(db.String(500))
    AccountId = db.Column(db.Integer, db.ForeignKey('account.AccountId'))

    def __init__(self, RatingId, Star, Description, AccountId):
        self.RatingId = RatingId
        self.Star = Star
        self.Description = Description
        self.AccountId = AccountId

    def __init__(self, Star, Description, AccountId):
        self.Star = Star
        self.Description = Description
        self.AccountId = AccountId

    def json(self):
        return {"RatingId": self.RatingId, "Star": self.Star,
                "Description": self.Description, "AccountId": self.AccountId}

    @classmethod
    def find_by_AccountId(cls, id):
        return cls.query.filter_by(AccountId=id).first()

    @classmethod
    def average(cls):
        ave = db.session.query(db.func.avg(Rating.Star))
        return round(ave, 2)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()