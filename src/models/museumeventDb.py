import datetime
from sqlalchemy.orm import relationship
from src.database import db

class Museumevent(db.Model):
    __tablename__  = 'museumevent'
    EventId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50))
    Description = db.Column(db.String(500))
    OpenTime = db.Column(db.Time)
    CloseTime = db.Column(db.Time)
    EventDate = db.Column(db.Date)
    Poster = db.Column(db.Integer, db.ForeignKey('image.ImageId'))
    Image = relationship("Image", foreign_keys=[Poster])

    def __init__(self, EventId, Name, Description, OpenTime, CloseTime, EventDate, Poster):
        self.EventId = EventId
        self.Name = Name
        self.Description = Description
        self.OpenTime = OpenTime
        self.CloseTime = CloseTime
        self.EventDate = EventDate
        self.Poster = Poster

    def json(self):
        if isinstance(self.OpenTime, datetime.time):
            self.OpenTime = self.OpenTime.strftime("%H:%M:%S")
        if isinstance(self.CloseTime, datetime.time):
            self.CloseTime = self.CloseTime.strftime("%H:%M:%S")
        if isinstance(self.EventDate, datetime.date):
            self.EventDate = self.EventDate.strftime("%Y-%m-%d")
        return {'EventId': self.EventId, 'Name': self.Name, 'Description' : self.Description, 'OpenTime' : self.OpenTime, 'CloseTime' : self.CloseTime, 'EventDate' : self.EventDate, 'Poster': self.Poster}


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(EventId=id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(Name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()