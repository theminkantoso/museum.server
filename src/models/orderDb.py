from src.database import db


class Order(db.Model):
    __tablename__ = 'orders'
    OrderId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    OrderDate = db.Column(db.Date)
    TotalPrice = db.Column(db.Integer)
    CreatedAt = db.Column(db.Date)
    QRCode = db.Column(db.String)
    used = db.Column(db.Boolean)

    def __init__(self, OrderId, OrderDate, TotalPrice, CreatedAt, QRCode, used):
        self.OrderId = OrderId
        self.OrderDate = OrderDate
        self.TotalPrice = TotalPrice
        self.CreatedAt = CreatedAt
        self.QRCode = QRCode
        self.used = used

    def __init__(self, OrderId, OrderDate, TotalPrice, CreatedAt, QRCode, used):
        self.OrderId = OrderId
        self.OrderDate = OrderDate
        self.TotalPrice = TotalPrice
        self.CreatedAt = CreatedAt
        self.QRCode = QRCode
        self.used = used

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def commit_to_db(self):
        db.session.commit()

    @classmethod
    def find_by_qr(cls, qr):
        return cls.query.filter_by(QRCode=qr).first()

    def json(self):
        return {'OrderId': self.OrderId, 'OrderDate': self.OrderDate, 'TotalPrice': self.TotalPrice,
                'CreatedAt': self.CreatedAt, 'QRCode': self.QRCode, 'used': self.used}
