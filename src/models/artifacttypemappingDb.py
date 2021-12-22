from src.database import db
from sqlalchemy.orm import relationship

class ArtifactTypeMapping(db.Model):
    __tablename__ = 'artifacttypemapping'
    ArtifactId = db.Column(db.Integer, db.ForeignKey('artifact.ArtifactId'), primary_key=True)
    ArtifactTypeId = db.Column(db.Integer, db.ForeignKey('artifacttype.ArtifactTypeId'), primary_key=True)
    # Khóa ngoại chỉ mục : INDEX
    Artifact = relationship("Artifact", foreign_keys=[ArtifactId])
    ArtifactType = relationship("ArtifactType", foreign_keys=[ArtifactTypeId])

    def __init__(self, ArtifactId, ArtifactTypeId):
        self.ArtifactId = ArtifactId
        self.ArtifactTypeId = ArtifactTypeId

    def json(self):
        return {'ArtifactId' : self.ArtifactId, 'ArtifactTypeId': self.ArtifactTypeId}

    #Tìm ArtifactId
    @classmethod
    def find_by_id1(cls, id):
        return cls.query.filter_by(ArtifactId=id).first()

    # Tìm ArtifactTypeId
    @classmethod
    def find_by_id2(cls, id):
        return cls.query.filter_by(ArtifactTypeId=id).first()

    #phân loại theo type
    @classmethod
    def find_by_id(cls, id):
        q = cls.query.filter_by(ArtifactTypeId=id)
        return q.all()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()