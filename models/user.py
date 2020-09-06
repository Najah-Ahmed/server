from db import db
from .booking import BookingModel
from .payment import PaymentModel
from .feedback import FeedbackModel
from .packages import PackagesModel
from itsdangerous import TimedJSONWebSignatureSerializer as serializer


class UsersModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(100))
    userName = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(5000))
    phoneNum = db.Column(db.String(80), unique=True)
    profile_img = db.Column(db.String(100), nullable=True,
                            )
    is_Admin = db.Column(db.Boolean, default='false')
    feedback = db.relationship(
        'FeedbackModel', backref='owner', lazy='dynamic')
    booking = db.relationship('BookingModel', backref='owner',  lazy='dynamic')
    packages = db.relationship(
        'PackagesModel', backref='owner',  lazy='dynamic')
    payment = db.relationship('PaymentModel', backref='owner',  lazy='dynamic')
    email_confirm = db.Column(db.Boolean, default='false')
    phoneNum_confirm = db.Column(db.Boolean, default='false')
    created_at = db.Column(db.DateTime)

    def __init__(self, fullName, userName, email, password, phoneNum, profile_img, is_Admin, email_confirm, phoneNum_confirm, created_at):
        self.fullName = fullName
        self.userName = userName
        self.email = email
        self.password = password
        self.phoneNum, = phoneNum,
        self.profile_img = profile_img
        self.email_confirm = email_confirm
        self.phoneNum_confirm = phoneNum_confirm
        self.is_Admin = is_Admin
        self.created_at = created_at
