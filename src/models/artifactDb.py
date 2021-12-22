from sqlalchemy.orm import relationship

from src.database import db

class Artifact(db.Model):
    __tablename__ = 'artifact'
    ArtifactId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50))
    Description = db.Column(db.String(500))
    Level = db.Column(db.Integer)
    ImageId = db.Column(db.Integer, db.ForeignKey('image.ImageId'))
    Image = relationship("Image", foreign_keys=[ImageId])

    def __init__(self,ArtifactId, Name, Description, Level, ImageId):
        self.ArtifactId = ArtifactId
        self.Name = Name
        self.Description = Description
        self.Level = Level
        self.ImageId = ImageId

    def json(self):
        return {'ArtifactId': self.ArtifactId,'Name' : self.Name, 'Description' : self.Description, 'Level' : self.Level,'ImageId' : self.ImageId}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(Name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(ArtifactId=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()