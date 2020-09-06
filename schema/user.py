from db import db

from marshmallow import fields, Schema
from models.user import UsersModel
from .feedback import FeedbackSchema
from .payment import PaymentSchema
from .booking import BookingSchema


class UsersSchema(Schema):
    # *** field u  like  to show
    class Meta:
        model = UsersModel
        sqla_session = db.session
    id = fields.Integer()
    fullName = fields.String()
    userName = fields.String()
    email = fields.Email()
    password = fields.String()
    phoneNum = fields.String()
    profile_img = fields.String()
    phoneNum_confirm = fields.Boolean()
    email_confirm = fields.Boolean()
    feedback = fields.Nested(FeedbackSchema, many=True, only=[
                             'comment', 'rating', 'created_at'])
    booking = fields.Nested(BookingSchema)
    payment = fields.Nested(PaymentSchema)
    is_Admin = fields.Boolean()
    created_at = fields.DateTime()
    # fields = ('id', 'fullName', 'userName', 'email', 'password',
    #           'phoneNum',  'is_Admin', 'created_at')

    # company = fields.Nested(CompanySchema)


user_schema = UsersSchema()  # show only single
# user_feedback_schema = UserFeedbackSchema()  # show only single
users_schema = UsersSchema(many=True)  # show all users
