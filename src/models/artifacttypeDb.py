from src.database import db

class  ArtifactType(db.Model):
        __tablename__ = 'artifacttype'
        ArtifactTypeId = db.Column(db.Integer, primary_key=True)
        Name = db.Column(db.String(50))
        def __init__(self,ArtifactTypeId, Name):
                self.ArtifactTypeId = ArtifactTypeId
                self.Name = Name

        def json(self):
                return {'ArtifactTypeId': self.ArtifactTypeId,'Name':self.Name}

        @classmethod
        def find_by_name(cls, name):
                return cls.query.filter_by(Name=name).first()

        @classmethod
        def find_by_id(cls, id):
                return cls.query.filter_by(ArtifactTypeId=id).first()

        def save_to_db(self):
                db.session.add(self)
                db.session.commit()

        def delete_from_db(self):
                db.session.delete(self)
                db.session.commit()