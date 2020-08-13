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
            # print(manta)

        else:
            bari = today + timedelta(days=1)
            booking = TicketModel.query.filter_by(
                arriced_place=arrived, destination_place=destination, date_of_day=bari).all()
            # print(bari)
        # print(booking)
        # return {"message": "get all tickets"}
        result = tickets_booking_schema.dump(booking)

        d = []
        if result == d:
            return {"message": "Empty Data"}, 400
        return {"data": result}


class BookingsResource(Resource):
    @jwt_required
    def get(self, booking_id):
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(
            email=user_from_token).first()
        id = booking_id
        booking = BookingModel.query.get(id)
        if not booking:
            return {"message": "Not found booking"}, 404
        if current_user.id == booking.user_id:
            records = db.session.query(BookingModel).all()

            for record in records:
                data = []
                booking_merge = [record.seat_no]
                data.append(booking_merge)
                print(data)

            result = booking_schema.dump(booking)
            return jsonify(result=result)
        return {"error": " You Dont have previlege to view other users bookings"}, 403

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
    # @jwt_required
    def get(self, ticket_id):
        tickets_booking = BookingModel.query.filter_by(
            ticket_id=ticket_id).all()
        for record in tickets_booking:
            data = []
            booking_merge = record.seat_no
            data.append(booking_merge)

            print(str(data))
        return{"message": "Thank For Booking Ticket"}

    @jwt_required
    def post(self, ticket_id):
        user_from_token = get_jwt_identity()
        user = UsersModel.query.filter_by(email=user_from_token).first()

        price = request.json['price']
        seat_no = request.json['seat_no']
        created_at = str(datetime.now())
        new_booking = BookingModel(
            user_id=user.id, ticket_id=ticket_id, price=price, seat_no=seat_no, created_at=created_at)
        db.session.add(new_booking)
        db.session.commit()
        return{"message": "Thank For Booking Ticket"}
