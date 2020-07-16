from flask import request, jsonify
from datetime import datetime

from flask_restful import Resource
from schema.booking import booking_schema, bookings_schema
from models.booking import BookingModel
from db import db


class BookingsList(Resource):
    def get(self):
        return {"message": "get all tickets"}

    def post(self):
        return {"message": "create tickets"}


class BookingsResource(Resource):
    def get(self, booking_id):
        return {"message": "get single booking {}".format(booking_id)}

    def put(self, booking_id):
        return {"message": "update single booking {}".format(booking_id)}

    def delete(self, booking_id):
        return {"message": "deleted single booking {}".format(booking_id)}
