from flask import request, jsonify
from datetime import datetime, timedelta

from flask_restful import Resource
from schema.tickets import ticket_schema, tickets_schema
from models.tickets import TicketModel
from models.user import UsersModel
from db import db
from flask_jwt_extended import jwt_required, get_jwt_identity


class TicketsList(Resource):
    def get(self):
        ticket = TicketModel.query.all()
        result = tickets_schema.dump(ticket)
        return {"data": result}

    @jwt_required
    def post(self):
        user_from_token = get_jwt_identity()
        user = UsersModel.query.filter_by(email=user_from_token).first()

        if user.is_Admin == True:
            arriced_place = request.json['arrivedPlace']
            destination_place = request.json['destination']
            bus_id = request.json['busId']  # check dublication in db
            bus_no_seat = request.json['busSeats']
            price_per_seat = request.json['pricePerSeat']
            time_of_journery = request.json['timeJournery']
            time_of_arrived = request.json['timeOfArrived']
            wakhtiga = request.json['wakhtiga']
            today = datetime.now().date()

            url = f"api/v1/ticket/"
            if wakhtiga == "manta":
                date_of_day = today

            else:
                date_of_day = today + timedelta(days=1)

            created_at = str(datetime.now())
            new_tickets = TicketModel(arriced_place, destination_place, bus_id, bus_no_seat,
                                      price_per_seat, url, time_of_journery, time_of_arrived, date_of_day, created_at)
            db.session.add(new_tickets)
            db.session.commit()
            return {"message": "create tickets"}
        return {"error": " NOT HAVE RIGHT PRIVAGE TO CREATE TRAVEL PLEASE CONTACT YOUR ADMIN"}, 403


class TicketsResource(Resource):
    def get(self, id):
        ticket = TicketModel.query.get(id)
        if not ticket:
            return {"error": "Not found Ticket"}, 404
        result = ticket_schema.dump(ticket)
        return jsonify(result=result)

    @jwt_required
    def put(self, id):
        user_from_token = get_jwt_identity()
        user = UsersModel.query.filter_by(email=user_from_token).first()
        if user.is_Admin == True:
            ticket = TicketModel.query.get(id)
            if not ticket:
                return {"message": "Not found Ticket"}, 404
            arriced_place = request.json['arrived_place']
            destination_place = request.json['destination_place']
            bus_id = request.json['bus_id']  # check dublication in db
            bus_no_seat = request.json['bus_on_seats']
            price_per_seat = request.json['price_per_seat']
            time_of_journery = request.json['time_of_journery']
            time_of_arrived = request.json['time_of_arrived']
            wakhtiga = request.json['wakhtiga']
            url = url = f"api/v1/ticket/{ticket.id}"
            today = datetime.now().date()
            if wakhtiga == "manta":
                date_of_day = today

            else:
                date_of_day = today + timedelta(days=1)

            ticket.arriced_place = arriced_place
            ticket.destination_place = destination_place
            ticket.bus_id = bus_id
            ticket.bus_no_seat = bus_no_seat
            ticket.price_per_seat = price_per_seat
            ticket.time_of_journery = time_of_journery
            ticket.time_of_arrived = time_of_arrived
            ticket.wakhtiga = wakhtiga
            ticket.date_of_day = date_of_day
            ticket.url = url
            print(ticket.url)
            db.session.commit()
            result = ticket_schema.dump(ticket)
            return jsonify(result)
        return {"message": " NOT HAVE RIGHT PRIVAGE TO UPDATE TRAVEL PLEASE CONTACT YOUR ADMIN"}, 403

    @jwt_required
    def delete(self, id):
        user_from_token = get_jwt_identity()
        user = UsersModel.query.filter_by(email=user_from_token).first()
        if user.is_Admin == True:
            ticket = TicketModel.query.get(id)
            if not ticket:
                return {"error": "Not found Ticket"}, 404
            db.session.delete(ticket)
            db.session.commit()
            return{"message": "Successfully deleted."}, 200
        return {"message": " NOT HAVE RIGHT PRIVAGE TO DELETE TRAVEL PLEASE CONTACT YOUR ADMIN"}, 403
