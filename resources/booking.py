from flask import request, jsonify
from datetime import datetime, timedelta

from flask_restful import Resource
from schema.booking import booking_schema, bookings_schema
from schema.tickets import tickets_booking_schema
from models.booking import BookingModel
from models.tickets import TicketModel
from models.user import UsersModel
from db import db
import itertools
from flask_jwt_extended import jwt_required, get_jwt_identity


class SearchTicket(Resource):
    def get(self):

        data = request.args
        arrived = data['arrived']
        destination = data['destination']
        wakhtiga = data['date']
        today = datetime.now().date()
        if wakhtiga == 'manta':
            manta = today
            booking = TicketModel.query.filter_by(
                arriced_place=arrived, destination_place=destination, date_of_day=manta).all()
        else:
            bari = today + timedelta(days=1)
            booking = TicketModel.query.filter_by(
                arriced_place=arrived, destination_place=destination, date_of_day=bari).all()
        result = tickets_booking_schema.dump(booking)

        d = []
        if result == d:
            return {"error": "Empty Data"}, 400
        return {"data": result}


class BookingsResource(Resource):

    def put(self, booking_id):
        return {"message": "refunding {}".format(booking_id)}

    @jwt_required
    def delete(self, booking_id):
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(
            email=user_from_token).first()
        id = booking_id
        booking = BookingModel.query.get(id)
        if not booking:
            return {"message": "Not found booking"}, 404
        if current_user.id == booking.user_id:
            db.session.delete(booking)
            db.session.commit()
            return{"message": " Successfully Cancel Please Call for refund Thank You."}, 200
        return {"error": " You Dont have previlege to cancel other users bookings"}, 403


class BookingTicket(Resource):

    @jwt_required
    def post(self, ticket_id):
        id = ticket_id
        user_from_token = get_jwt_identity()
        user = UsersModel.query.filter_by(email=user_from_token).first()
        ticket = TicketModel.query.get(id)
        if not ticket:
            return {"message": "Not found booking"}, 404
        price = request.json['price']
        seat_no = request.json['seat_no']
        # counterSeat = request.json['counterSeat']

        # price = ticket.price_per_seat*counterSeat
        # print(price)

        created_at = str(datetime.now())
        new_booking = BookingModel(
            user_id=user.id, ticket_id=ticket_id, price=price, seat_no=seat_no, created_at=created_at)
        db.session.add(new_booking)
        db.session.commit()
        return{"message": "Thank For Booking Ticket"}


class BookingList(Resource):
    @jwt_required
    def get(self):
        user_from_token = get_jwt_identity()
        user = UsersModel.query.filter_by(email=user_from_token).first()
        if user.is_Admin == True:
            result = BookingModel.query.all()
            data = bookings_schema.dump(result)
            return jsonify(data=data)
        return{"error": "you don't have sufficient privileges to view all users please Contact Your Admin"}, 401


class SingleUserBooking(Resource):
    @jwt_required
    def get(self):
        user_from_token = get_jwt_identity()
        user = UsersModel.query.filter_by(email=user_from_token).first()
        id = user.id
        result = BookingModel.query.filter_by(id=id).all()
        data = bookings_schema.dump(result)
        return jsonify(data=data)
