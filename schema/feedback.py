from db import db

from marshmallow import fields,Schema
from models.feedback import FeedbackModel
from models.user import UsersModel



class FeedbackSchema(Schema):
    # *** field like to show
    

    # class Meta:
    #      fields = ('comment', 'rating', 'owner_id','created_at')
    class Meta:
        model = UsersModel
        sqla_session=db.session
        
    comment = fields.String()
    rating= fields.Float()
    owner_id=fields.Integer()
    tickter_id=fields.Integer()
    created_at = fields.DateTime()


feedback_schema = FeedbackSchema()
feedbacks_schema = FeedbackSchema(many=True)
