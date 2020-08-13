from flask import request, jsonify
from datetime import datetime, timedelta

from flask_restful import Resource
from schema.payment import payment_schema, payments_schema
from models.payment import PaymentModel
from models.booking import BookingModel
from models.packages import PaymentModel
from models.user import UsersModel
from db import db
from flask_jwt_extended import jwt_required, get_jwt_identity


class PaymentsList(Resource):
    def get(self):
        return {"message": "get all tickets"}


class PaymentsResource(Resource):
    def get(self, tran_id):
        return {"message": "get single tran {}".format(tran_id)}

    def put(self, tran_id):
        return {"message": "update single tran {}".format(tran_id)}

    def delete(self, tran_id):
        return {"message": "deleted single tran {}".format(tran_id)}


class PaymentBooking(Resource):
    @jwt_required
    def post(self, booking_id):
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(
            email=user_from_token).first()
        fullname = request.json['fullname']
        method_of_pay = request.json['method_of_pay']
        id = booking_id
        booking = BookingModel.query.get(id)
        booking_amount = booking.price
        created_at = str(datetime.now())
        new_trans = PaymentModel(user_id=current_user.id, booking_id=booking_id, package_id=None, amount=booking_amount,
                                 fullname=fullname, method_of_pay=method_of_pay, created_at=created_at)
        db.session.add(new_trans)
        db.session.commit()
        return {"message": "Successfully Transcation Thank You for Using Services"}


class PaymentPacakage(Resource):
    def post(self, packages_id):
        return {"message": "create tickets"}
