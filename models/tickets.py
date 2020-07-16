from db import db
from .booking import BookingModel
from .feedback import FeedbackModel
# **** Tickets Model


class TicketModel(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key=True)
    arriced_place = db.Column(db.String(50))
    destination_place = db.Column(db.String(80))
    bus_id = db.Column(db.Integer)
    bus_no_seat = db.Column(db.Integer)
    price_per_seat = db.Column(db.Float)
    time_of_journery = db.Column(db.Time)
    time_of_arrived = db.Column(db.Time)
    url=db.Column(db.String(50))
    booking = db.relationship(
        'BookingModel', backref='ticket', lazy='dynamic')
    feedback = db.relationship(
        'FeedbackModel', backref='ticket', lazy='dynamic')
    created_at = db.Column(db.DateTime)

    def __init__(self, arriced_place, destination_place, bus_id, bus_no_seat, price_per_seat, url,time_of_journery, time_of_arrived, created_at):
        self.arriced_place = arriced_place
        self.destination_place = destination_place
        self. bus_id = bus_id
        self.bus_no_seat = bus_no_seat
        self.price_per_seat = price_per_seat
        self.time_of_journery = time_of_journery
        self.time_of_arrived = time_of_arrived
        self.url = url
        self.created_at = created_at

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()
