from flask import request, jsonify
from datetime import datetime, timedelta
from flask_restful import Resource
from schema.package import package_schema, packages_schema
from models.packages import PackagesModel
from models.user import UsersModel
from db import db
from flask_jwt_extended import jwt_required, get_jwt_identity


class PackageList(Resource):

    @jwt_required
    def get(self):
        user_from_token = get_jwt_identity()
        user = UsersModel.query.filter_by(email=user_from_token).first()
        if user.is_Admin == True:
            package = PackagesModel.query.all()
            result = packages_schema.dump(package)
            return {"packages": result}

        return {"error": " NOT HAVE RIGHT VIEW THE PACKAGES PLEASE CONTACT YOUR ADMIN"}, 403

    @jwt_required
    def post(self):
        user_from_token = get_jwt_identity()
        user = UsersModel.query.filter_by(email=user_from_token).first()
        receiver_to_user = request.json['receiversName']
        receiver_to_place = request.json['receiversDestination']
        receiver_phone_number = request.json['receiversPhone']
        descriptions = request.json['descp']
        sender_user_id = user.id
        receiver_confirm = 0
        price = request.json['price']

        created_at = str(datetime.now())

        if descriptions == '':
            descriptions = 'this is packages ahah'
            new_package = PackagesModel(receiver_phone_number=receiver_phone_number, receiver_to_place=receiver_to_place,
                                        receiver_to_user=receiver_to_user,  receiver_confirm=receiver_confirm, price=price, descriptions=descriptions, sender_user_id=sender_user_id,  created_at=created_at)
            db.session.add(new_package)
            db.session.commit()
        new_package = PackagesModel(receiver_phone_number=receiver_phone_number, receiver_to_place=receiver_to_place,
                                    receiver_to_user=receiver_to_user,  receiver_confirm=receiver_confirm, price=price, descriptions=descriptions, sender_user_id=sender_user_id,  created_at=created_at)
        db.session.add(new_package)
        db.session.commit()
        return {"message": "successfully sent package Thank You"}


class PackagesResources(Resource):
    def get(self, package_id):
        id = package_id
        package = PackagesModel.query.get(id)
        if not package:
            return {"error": "Not found package"}, 404
        result = package_schema.dump(package)
        return jsonify(result=result)

    @jwt_required
    def put(self, package_id):
        id = package_id
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(
            email=user_from_token).first()
        package = PackagesModel.query.get(id)
        if not package:
            return {"message": "Not found Feeback"}, 404
        if current_user.id == package.id:
            receiver_to_user = request.json['receiversName']
            receiver_to_place = request.json['receiversDestination']
            receiver_phone_number = request.json['receiversPhone']
            descriptions = request.json['descp']
            price = request.json['price']
            receiver_confirm = request.json['receiver_confirm']

            if receiver_confirm == True:
                package.receiver_to_user = receiver_to_user
                package.receiver_to_place = receiver_to_place
                package.receiver_phone_number = receiver_phone_number
                package.descriptions = descriptions
                package.price = price
                package.receiver_confirm = receiver_confirm

                db.session.commit()
                result = package_schema.dump(package)
                return jsonify(result)
            return {"error": "not allow to null"}
        return {"error": " You Dont have previlege to update other users senting packages"}, 403

    @jwt_required
    def delete(self, package_id):
        id = package_id
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(
            email=user_from_token).first()
        package = PackagesModel.query.get(id)
        print(current_user.id)
        print(package.sender_user_id)
        if not package:
            return {"message": "Not found Packages"}, 404
        if current_user.id == package.sender_user_id:

            db.session.delete(package)
            db.session.commit()
            return{"message": " Successfully deleted."}, 200

        return {"error": " You Dont have previlege to delete other senting packages"}, 403


class SingleUserPackages(Resource):
    @jwt_required
    def get(self):
        user_from_token = get_jwt_identity()
        user = UsersModel.query.filter_by(email=user_from_token).first()
        id = user.id
        result = PackagesModel.query.filter_by(id=id).all()
        data = packages_schema.dump(result)
        return jsonify(data=data)
