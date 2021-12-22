from src.database import db


class AgeGroup(db.Model):
    __tablename__ = 'agegroup'
    GroupId = db.Column(db.Integer, primary_key=True)
    Description = db.Column(db.String)
    Price = db.Column(db.Integer)

    def __init__(self, GroupId, Description, Price):
        self.GroupId = GroupId
        self.Description = Description
        self.Price = Price

    def json(self):
        return {'GroupId': self.GroupId, 'Description': self.Description, 'Price': self.Price}
