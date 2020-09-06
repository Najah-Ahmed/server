from flask import request, jsonify
from datetime import datetime, timedelta

from flask_restful import Resource
from schema.payment import payment_schema, payments_schema
from models.payment import PaymentModel
from models.booking import BookingModel
from models.packages import PackagesModel
from models.packages import PaymentModel
from models.user import UsersModel
from db import db
from flask_jwt_extended import jwt_required, get_jwt_identity


class PaymentsList(Resource):
    @jwt_required
    def get(self):
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(
            email=user_from_token).first()
        if current_user.is_Admin == True:
            payment = PaymentModel.query.all()
            result = payments_schema.dump(payment)
            return {"data": result}

        return{"error": "you don't have sufficient privileges to view all Bookings please Contact Your Admin"}, 401


class PaymentBooking(Resource):
    @jwt_required
    def post(self, booking_id):
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(
            email=user_from_token).first()
        fullname = request.json['fullname']
        method_of_pay = request.json['method_of_pay']
        phoneNum = request.json['phoneNum']
        id = booking_id
        booking = BookingModel.query.get(id)
        booking_amount = booking.price
        created_at = str(datetime.now())
        new_trans = PaymentModel(user_id=current_user.id, booking_id=booking_id, package_id=None, amount=booking_amount,
                                 phoneNum=phoneNum, fullname=fullname, method_of_pay=method_of_pay, created_at=created_at)
        db.session.add(new_trans)
        db.session.commit()
        return {"message": "Successfully Transcation Thank You for Using Services"}


class PaymentPacakage(Resource):
    @jwt_required
    def post(self, package_id):
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(
            email=user_from_token).first()
        fullname = request.json['fullname']
        method_of_pay = request.json['method_of_pay']
        phoneNum = request.json['phoneNum']
        id = package_id
        package = PackagesModel.query.get(id)
        package_amount = package.price
        created_at = str(datetime.now())
        new_trans = PaymentModel(user_id=current_user.id, booking_id=None, package_id=package_id, amount=package_amount,
                                 phoneNum=phoneNum, fullname=fullname, method_of_pay=method_of_pay, created_at=created_at)
        db.session.add(new_trans)
        db.session.commit()
        return {"message": "Successfully Transcation Thank You for Using Services"}


class SingleUserPayment(Resource):
    @jwt_required
    def get(self):
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(
            email=user_from_token).first()
        user_id = current_user.id
        payment = PaymentModel.query.filter_by(user_id=user_id).all()
        result = payments_schema.dump(payment)
        return jsonify(result=result)
