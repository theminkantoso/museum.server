from src.database import db
from src.models.ticketDb import TicketDb
from src.models.ageGroupDb import AgeGroupDb
from src.models.orders_souvenirDb import OrderSouvernirDetailDb
from src.models.souvenirDb import SouvenirDb


class OrderDb(db.Model):
    __tablename__ = 'orders'
    OrderId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    OrderDate = db.Column(db.Date)
    TotalPrice = db.Column(db.Integer)
    CreatedAt = db.Column(db.Date)
    AccountId = db.Column(db.Integer)
    QRCode = db.Column(db.String)
    used = db.Column(db.Boolean)
    type = db.Column(db.Integer)

    # def __init__(self, OrderId, OrderDate, TotalPrice, CreatedAt, QRCode, used):
    #     self.OrderId = OrderId
    #     self.OrderDate = OrderDate
    #     self.TotalPrice = TotalPrice
    #     self.CreatedAt = CreatedAt
    #     self.QRCode = QRCode
    #     self.used = used

    def __init__(self, OrderDate, TotalPrice, CreatedAt, AccountId, QRCode, type):
        self.OrderDate = OrderDate
        self.TotalPrice = TotalPrice
        self.CreatedAt = CreatedAt
        self.QRCode = QRCode
        self.AccountId = AccountId
        self.used = False
        self.type = type

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def commit_to_db(self):
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(OrderId=id).first()

    @classmethod
    def find_by_qr(cls, qr):
        return cls.query.filter_by(QRCode=qr).first()

    @staticmethod
    def qr_detail_ticket(qr):
        return db.session.query(TicketDb.NumberPerson, AgeGroupDb.Description).select_from(OrderDb).\
            join(TicketDb, OrderDb.OrderId == TicketDb.OrderId).\
            join(AgeGroupDb, TicketDb.TicketType == AgeGroupDb.GroupId).filter(OrderDb.QRCode == qr).\
            filter(OrderDb.type == 0).all()

    @staticmethod
    def qr_detail_order_sou(qr):
        return db.session.query(OrderSouvernirDetailDb.Quantity, SouvenirDb.Name).\
            select_from(OrderDb).join(OrderSouvernirDetailDb, OrderDb.OrderId == OrderSouvernirDetailDb.OrderId). \
            join(SouvenirDb, OrderSouvernirDetailDb.SouvernirId == SouvenirDb.SouvenirId).filter(OrderDb.QRCode == qr).\
            filter(OrderDb.type == 1).all()

    @classmethod
    def find_by_account_ticket(cls, id):
        return cls.query.filter_by(AccountId=id).filter_by(type=0).all()

    @classmethod
    def find_by_account_order(cls, id):
        return cls.query.filter_by(AccountId=id).filter_by(type=1).all()

    @staticmethod
    def stats_order_all():
        return db.session.query(db.func.sum(OrderSouvernirDetailDb.Quantity), SouvenirDb.Name).\
            select_from(OrderDb).join(OrderSouvernirDetailDb, OrderDb.OrderId == OrderSouvernirDetailDb.OrderId).\
            join(SouvenirDb, OrderSouvernirDetailDb.SouvenirId == SouvenirDb.SouvenirId).\
            group_by(SouvenirDb.SouvenirId).filter(OrderDb.type == 1).all()

    @staticmethod
    def stats_order_by_date(date):
        return db.session.query(db.func.sum(OrderSouvernirDetailDb.Quantity), SouvenirDb.Name). \
            select_from(OrderDb).join(OrderSouvernirDetailDb, OrderDb.OrderId == OrderSouvernirDetailDb.OrderId). \
            join(SouvenirDb, OrderSouvernirDetailDb.SouvenirId == SouvenirDb.SouvenirId). \
            group_by(SouvenirDb.SouvenirId).filter(OrderDb.type == 1).filter(OrderDb.OrderDate == date).all()

    @staticmethod
    def stats_ticket_all():
        return db.session.query(db.func.sum(TicketDb.NumberPerson), AgeGroupDb.Description). \
            select_from(OrderDb).join(TicketDb, OrderDb.OrderId == TicketDb.OrderId). \
            join(AgeGroupDb, TicketDb.TicketType == AgeGroupDb.GroupId).\
            group_by(AgeGroupDb.GroupId).filter(OrderDb.type == 0).all()

    @staticmethod
    def stats_ticket_by_date(date):
        return db.session.query(db.func.sum(TicketDb.NumberPerson), AgeGroupDb.Description). \
            select_from(OrderDb).join(TicketDb, OrderDb.OrderId == TicketDb.OrderId). \
            join(AgeGroupDb, TicketDb.TicketType == AgeGroupDb.GroupId). \
            group_by(AgeGroupDb.GroupId).filter(OrderDb.type == 0).filter(OrderDb.OrderDate == date).all()

    @staticmethod
    def total_price_ticket_all():
        return db.session.query(db.func.sum(OrderDb.TotalPrice)).filter(OrderDb.type == 0).all()

    @staticmethod
    def total_price_ticket_date(date):
        return db.session.query(db.func.sum(OrderDb.TotalPrice)).filter(OrderDb.type == 0).\
            filter(OrderDb.OrderDate == date).all()

    def json(self):
        if self.type == 0:
            order_type = 'Ve vao'
        elif self.type == 1:
            order_type = 'Don dat'
        return {'OrderId': self.OrderId, 'OrderDate': self.OrderDate, 'TotalPrice': self.TotalPrice,
                'CreatedAt': self.CreatedAt, 'QRCode': self.QRCode, 'used': self.used, 'order_type': order_type}
