from src.database import db
from src.models.ticketDb import TicketDb
from src.models.ageGroupDb import AgeGroupDb


class OrderDb(db.Model):
    __tablename__ = 'orders'
    OrderId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    OrderDate = db.Column(db.Date)
    TotalPrice = db.Column(db.Integer)
    CreatedAt = db.Column(db.Date)
    AccountId = db.Column(db.Integer)
    QRCode = db.Column(db.String)
    used = db.Column(db.Boolean)

    # def __init__(self, OrderId, OrderDate, TotalPrice, CreatedAt, QRCode, used):
    #     self.OrderId = OrderId
    #     self.OrderDate = OrderDate
    #     self.TotalPrice = TotalPrice
    #     self.CreatedAt = CreatedAt
    #     self.QRCode = QRCode
    #     self.used = used

    def __init__(self, OrderDate, TotalPrice, CreatedAt, AccountId, QRCode):
        self.OrderDate = OrderDate
        self.TotalPrice = TotalPrice
        self.CreatedAt = CreatedAt
        self.QRCode = QRCode
        self.AccountId = AccountId
        self.used = False

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def commit_to_db(self):
        db.session.commit()

    @classmethod
    def find_by_qr(cls, qr):
        return cls.query.filter_by(QRCode=qr).first()

    @staticmethod
    def qr_detail_ticket(qr):
        return db.session.query(OrderDb.OrderDate, TicketDb.NumberPerson, AgeGroupDb.Description).select_from(OrderDb).\
            join(TicketDb, OrderDb.OrderId == TicketDb.OrderId).\
            join(AgeGroupDb, TicketDb.TicketType == AgeGroupDb.GroupId).filter(OrderDb.QRCode == qr).all()

    @classmethod
    def find_by_account(cls, id):
        return cls.query.filter_by(AccountId=id).first()

    def json(self):
        return {'OrderId': self.OrderId, 'OrderDate': self.OrderDate, 'TotalPrice': self.TotalPrice,
                'CreatedAt': self.CreatedAt, 'QRCode': self.QRCode, 'used': self.used}
