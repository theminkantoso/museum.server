from src.database import db


class OrderSouvernirDetailDb:
    __tablename__ = 'orderssouvenirdetail'
    OrderId = db.Column(db.Integer, db.ForeignKey("orders.OrderId"), primary_key=True)
    SouvernirId = db.Column(db.Integer, db.ForeignKey("souvenir.SouvenirId"), primary_key=True)
    Quantity = db.Column(db.Integer)

    def __init__(self, orderId, souvernirId, quantity):
        self.OrderId = orderId
        self.SouvernirId = souvernirId
        self.Quantity = quantity

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def commit_to_db(self):
        db.session.commit()
