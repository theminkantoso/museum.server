from src.database import db


class OrderSouvernirDetailDb:
    __tablename__ = 'orderssouvenirdetail'
    OrderId = db.Column(db.Integer, db.ForeignKey("orders.OrderId"), primary_key=True)
    SouvernirId = db.Column(db.Integer, db.ForeignKey("souvenir.SouvenirId"), primary_key=True)
    Quantity = db.Column(db.Integer)
