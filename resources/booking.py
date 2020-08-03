from flask import request, jsonify
from datetime import datetime,timedelta

from flask_restful import Resource
from schema.booking import booking_schema, bookings_schema
from schema.tickets import tickets_booking_schema
from models.booking import BookingModel
from models.tickets import TicketModel
from db import db


class BookingsList(Resource):
    def get(self):
      
      data=request.args
      arrived=data['arrived']
      destination=data['destination']
      wakhtiga=data['date']
      today = datetime.now().date()
      if wakhtiga=='manta':
        manta = today
        booking=TicketModel.query.filter_by(arriced_place=arrived,destination_place=destination,date_of_day=manta).all()
        print(manta)
            
      else:
        bari=today + timedelta(days = 1) 
        booking=TicketModel.query.filter_by(arriced_place=arrived,destination_place=destination,date_of_day=bari).all()
        print(bari)
      # print(booking)
      # return {"message": "get all tickets"}
      result = tickets_booking_schema.dump(booking)
      return {"data": result}








class BookingsResource(Resource):
    def get(self, booking_id):
        return {"message": "get single booking {}".format(booking_id)}

    def put(self, booking_id):
        return {"message": "update single booking {}".format(booking_id)}

    def delete(self, booking_id):
        return {"message": "deleted single booking {}".format(booking_id)}


class SearchTicket(Resource):
    def get(self):
      return {"message": "get all tickets"}
    def post(self):
      return {"message": "create tickets"}