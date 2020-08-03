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
    created_at = db.Column(db.DateTime)

    def __init__(self, comment, rating, created_at,owner_id ,ticket_id):
        self.comment = comment
        self.rating = rating
        self.owner_id = owner_id
        self.ticket_id = ticket_id
        self.created_at = created_at
