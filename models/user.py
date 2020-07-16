from db import db
from .booking import BookingModel
from .payment import PaymentModel
from .feedback import FeedbackModel
from itsdangerous import TimedJSONWebSignatureSerializer as serializer




class UsersModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(100))
    userName = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(5000))
    phoneNum = db.Column(db.String(80), unique=True)
    # profile_img = db.Column(db.String(100), nullable=False,
    #                         default='default.jpg')
    is_Admin = db.Column(db.Boolean, default='false')
    feedback = db.relationship(
        'FeedbackModel', backref='owner', lazy='dynamic')
    booking = db.relationship('BookingModel', backref='owner',  lazy='dynamic')
    payment = db.relationship('PaymentModel', backref='owner',  lazy='dynamic' )
    created_at = db.Column(db.DateTime)
    
    
    
    # def reset_user_password(self,expired_time=18000):
    #   s=serializer(SERCET_KEY,expired_time)
    #   return s.dumps({'user_email':self.email}).decode('utf-8')
    
    
    # @staticmethod
    # def verify_reset_token(token):
    #   s=serializer(SERCET_KEY)
    #   try:
    #     user_email=s.loads(token)['user_email']
    #   except:
    #     return {"error":"invalid token "}
    #   return UsersModel.query.get(user_email)
      
      

    def __init__(self, fullName, userName, email, password, phoneNum,  is_Admin,created_at):
        self.fullName = fullName
        self.userName = userName
        self.email = email
        self.password = password
        self.phoneNum, = phoneNum,
        # self.profile_img = profile_img
        # self.feedback = feedback
        # self.payment = payment
        # self.booking = booking
        self.is_Admin = is_Admin
        self.created_at = created_at

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
