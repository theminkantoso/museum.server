from src.database import db


class OrderSouvernirDetailDb(db.Model):
    __tablename__ = 'orderssouvenirdetail'
    OrderId = db.Column(db.Integer, db.ForeignKey("orders.OrderId"), primary_key=True, nullable=False)
    SouvenirId = db.Column(db.Integer, db.ForeignKey("souvenir.SouvenirId"), primary_key=True, nullable=False)
    Quantity = db.Column(db.Integer)

    def __init__(self, orderId, souvernirId, quantity):
        self.OrderId = orderId
        self.SouvenirId = souvernirId
        self.Quantity = quantity

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def commit_to_db(self):
        db.session.commit()
