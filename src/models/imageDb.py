import base64
from src.database import db


class Image(db.Model):
    __tablename__ = 'image'
    ImageId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(50))
    Content = db.Column(db.String(100))
    Url = db.Column(db.String(100))
    Path = db.Column(db.String(100))
    MimeType = db.Column(db.String(100))



    def __init__(self, ImageId, Name, Content, Url, Path, MimeType):
        self.ImageId = ImageId
        self.Name = Name
        self.Content = Content
        self.Url = Url
        self.Path = Path
        self.MimeType = MimeType

    def __init__(self, Name, Content, Url, Path, MimeType):
        self.Name = Name
        self.Content = Content
        self.Url = Url
        self.Path = Path
        self.MimeType = MimeType


    def json(self):
        # self.Url = str(self.Url)
        return {'ImageId': self.ImageId, 'Name': self.Name, 'Content': self.Content, 'Url': self.Url, 'Path': self.Path,
                'MimeType': self.MimeType}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(Name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(ImageId=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
