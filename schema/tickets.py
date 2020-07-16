from db import db
from models.tickets import TicketModel
from marshmallow import fields,Schema
from .feedback import FeedbackSchema

class TicketSchema(Schema):
    # *** field like to show
    # model = TicketModel

    # class Meta:
    #     fields = ('id', 'arriced_place', 'destination_place', 'bus_id', 'bus_no_seat',
    #               'price_per_seat', 'time_of_journery', 'time_of_arrived', 'created_at')
      class Meta:
        model = TicketModel
        sqla_session=db.session
        
        
      id=fields.Integer()
      arriced_place = fields.String()
      destination_place = fields.String()
      bus_id=fields.Integer()
      bus_no_seat=fields.Integer()
      price_per_seat=fields.Float()
      time_of_journery = fields.DateTime()
      time_of_arrived = fields.DateTime()
      feedback = fields.Nested(FeedbackSchema ,many=True, only=['comment','rating','created_at','owner_id'])
      url=fields.Url()
      created_at = fields.DateTime()


ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)
