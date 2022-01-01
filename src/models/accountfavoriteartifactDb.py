from src.database import db
from sqlalchemy.orm import relationship

class AccountFA(db.Model):
    __tablename__ = 'accountfavoriteartifact'
    AccountId = db.Column(db.Integer, db.ForeignKey('account.AccountId'), primary_key=True)
    ArtifactId = db.Column(db.Integer, db.ForeignKey('artifact.ArtifactId'), primary_key=True)
    # # Khóa ngoại chỉ mục : INDEX

    def __init__(self, AccountId, ArtifactId):
        self.AccountId = AccountId
        self.ArtifactId = ArtifactId

    def json(self):
        return {'AccountId': self.AccountId, 'ArtifactId': self.ArtifactId}


    @classmethod
    def find_by_id(cls, id1, id2):
        return cls.query.filter_by(AccountId=id1, ArtifactId=id2).first()


    #phân loại theo account
    @classmethod
    def find_by_id1(cls, id):
        q = cls.query.filter_by(AccountId=id)
        return q.all()



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()