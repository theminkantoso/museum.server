from src.database import db


class TicketDb(db.Model):
    __tablename__ = 'entryticket'
    TicketId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    OrderId = db.Column(db.Integer, db.ForeignKey('orders.OrderId'))
    NumberPerson = db.Column(db.Integer)
    TicketType = db.Column(db.Integer, db.ForeignKey('agegroup.GroupId'))

    def __init__(self, OrderId, NumberPerson, TicketType):
        self.OrderId = OrderId
        self.NumberPerson = NumberPerson
        self.TicketType = TicketType

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {'TicketId': self.TicketId, 'OrderId': self.OrderId, 'NumberPerson': self.NumberPerson,
                'TicketType': self.TicketType}


