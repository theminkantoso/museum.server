from src.database import db
from sqlalchemy.orm import relationship

class Souvenir(db.Model):
        __tablename__ = 'souvenir'
        SouvenirId = db.Column(db.Integer, primary_key=True)
        Name = db.Column(db.String(50))
        Description = db.Column(db.String(500))
        Price = db.Column(db.Integer)
        Discount = db.Column(db.Float)
        ImageId = db.Column(db.Integer, db.ForeignKey('image.ImageId'))
        #Image = relationship("Image", foreign_keys=[ImageId])

        def __init__(self,SouvenirId, Name, Description, Price, Discount, ImageId):
                self.SouvenirId = SouvenirId
                self.Name = Name
                self.Description = Description
                self.Price = Price
                self.Discount = Discount
                self.ImageId = ImageId

        def json(self):
                return {'SouvenirId': self.SouvenirId,'Name': self.Name, 'Description': self.Description, 'Price': self.Price,
                        'Discount': self.Discount, 'ImageId': self.ImageId}

        @classmethod
        def find_by_name(cls, name):
                return cls.query.filter_by(Name=name).first()

        @classmethod
        def find_by_id(cls, id):
                return cls.query.filter_by(SouvenirId=id).first()

        def save_to_db(self):
                db.session.add(self)
                db.session.commit()

        def delete_from_db(self):
                db.session.delete(self)
                db.session.commit()