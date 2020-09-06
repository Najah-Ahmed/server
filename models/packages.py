from db import db
from .payment import PaymentModel
# **** Packages Model


class PackagesModel(db.Model):
    __tablename__ = 'packages'
    id = db.Column(db.Integer, primary_key=True)
    receiver_to_user = db.Column(db.String(50))
    receiver_to_place = db.Column(db.String(50))
    receiver_phone_number = db.Column(db.String(80))
    descriptions = db.Column(db.Text)
    sender_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    payment = db.relationship(
        'PaymentModel', backref='packages', lazy='dynamic')
    price = db.Column(db.Float)
    receiver_confirm = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)

    def __init__(self, receiver_phone_number,  receiver_to_place, receiver_to_user, descriptions, receiver_confirm, price, sender_user_id,  created_at):
        self.receiver_to_user = receiver_to_user
        self.receiver_to_place = receiver_to_place
        self.receiver_phone_number = receiver_phone_number
        self.sender_user_id = sender_user_id
        self.price = price
        self.receiver_confirm = receiver_confirm
        self.descriptions = descriptions
        self.created_at = created_at
