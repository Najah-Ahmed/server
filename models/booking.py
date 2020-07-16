from db import db
from .payment import PaymentModel
# **** Booking Model


class BookingModel(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'))
    payment = db.relationship(
        'PaymentModel', backref='booking', lazy='dynamic')
    price = db.Column(db.Float)
    seat_no = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)

    def __init__(self, user_id, ticket_id, price, seat_no, created_at):
        self.user_id = user_id
        self.ticket_id = ticket_id
        self.price = price
        self.seat_no = seat_no
        self.created_at = created_at
