from db import db
from ma import ma
from models.tickets import TicketModel
from marshmallow import fields

from .feedback import FeedbackSchema


class TicketSchema(ma.Schema):
    # *** field like to show
    # model = TicketModel

    # class Meta:
    #     fields = ('id', 'arriced_place', 'destination_place', 'bus_id', 'bus_no_seat',
    #               'price_per_seat', 'time_of_journery', 'time_of_arrived', 'created_at')
    class Meta:
        model = TicketModel
        sqla_session = db.session

    id = fields.Integer()
    arriced_place = fields.String()
    destination_place = fields.String()
    bus_id = fields.Integer()
    bus_no_seat = fields.Integer()
    price_per_seat = fields.Float()
    time_of_journery = fields.DateTime()
    time_of_arrived = fields.DateTime()
    feedback = fields.Nested(FeedbackSchema, many=True, only=[
                             'comment', 'rating', 'created_at', 'owner_id'])
    url = fields.Url()
    date_of_day = fields.DateTime()
    created_at = fields.DateTime()


class TicketBookingSchema(ma.Schema):
    # *** field like to show
    class Meta:
        model = TicketModel
        sqla_session = db.session

    id = fields.Integer()
    arriced_place = fields.String()
    destination_place = fields.String()
    bus_id = fields.Integer()
    bus_no_seat = fields.Integer()
    price_per_seat = fields.Float()
    time_of_journery = fields.DateTime()
    time_of_arrived = fields.DateTime()
    url = fields.Url()
    date_of_day = fields.DateTime()
    created_at = fields.DateTime()


ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)
tickets_booking_schema = TicketBookingSchema(many=True)
