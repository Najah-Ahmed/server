from flask import request, jsonify
from datetime import datetime

from flask_restful import Resource
from schema.payment import payment_schema, payments_schema
from models.payment import PaymentModel
from db import db


class PaymentsList(Resource):
    def get(self):
        return {"message": "get all tickets"}

    def post(self):
        return {"message": "create tickets"}


class PaymentsResource(Resource):
    def get(self, tran_id):
        return {"message": "get single tran {}".format(tran_id)}

    def put(self, tran_id):
        return {"message": "update single tran {}".format(tran_id)}

    def delete(self, tran_id):
        return {"message": "deleted single tran {}".format(tran_id)}
