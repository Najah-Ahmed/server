from db import db

# **** payment Model


class PaymentModel(db.Model):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50))
    method_of_pay = db.Column(db.String(100))
    amount = db.Column(db.Float)
    phoneNum = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    booking_id = db.Column(
        db.Integer, db.ForeignKey('booking.id'), nullable=True)
    package_id = db.Column(db.Integer, db.ForeignKey(
        'packages.id'), nullable=True)
    created_at = db.Column(db.DateTime)

    def __init__(self, user_id, booking_id, phoneNum, package_id, amount, fullname, method_of_pay, created_at):
        self.user_id = user_id
        self.booking_id = booking_id
        self.phoneNum = phoneNum
        self.package_id = package_id
        self.fullname = fullname
        self.amount = amount
        self.method_of_pay = method_of_pay
        self.created_at = created_at
