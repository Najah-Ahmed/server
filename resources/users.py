from flask import request, jsonify, Response, render_template
from datetime import datetime, timedelta
from flask_restful import Resource
from schema.user import user_schema, users_schema
from models.user import UsersModel
from db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_raw_jwt
from flask_mail import Message


# email confirmed
# phone confired
# sent email or phone to forgetpassword


class UserRegister(Resource):

    def post(self):
        fullName = request.json['fullName']
        userName = request.json['username']
        email = request.json['email']
        password = request.json['password']
        phoneNum = request.json['phoneNum']
        is_Admin = 0
        created_at = str(datetime.now())
        check_email = UsersModel.query.filter_by(email=email).first()
        check_userName = UsersModel.query.filter_by(userName=userName).first()
        check_phoneNum = UsersModel.query.filter_by(phoneNum=phoneNum).first()
        if check_email:
            return {'error': 'An email {}  already exist.'.format(email)}, 400
        elif check_phoneNum:
            return {'error': 'An phoneNum {}  already exist.'.format(phoneNum)}, 400
        elif check_userName:
            return {'error': 'An userName {}  already used.'.format(userName)}, 400
        else:
            hash_password = generate_password_hash(password)
            new_user = UsersModel(fullName, userName, email,
                                  hash_password, phoneNum, is_Admin, created_at)

            db.session.add(new_user)
            db.session.commit()
            return{"message": "User created successfully."}, 201


class UserLogin(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password']
        check_email = UsersModel.query.filter_by(email=email).first()
        if not check_email:
            return {'error': 'Not found email '}, 404
        user = UsersModel.query.filter_by(email=email).first()
        check_password = check_password_hash(user.password, password)
        if not check_password:
            return {'error': 'wrong password'}, 400
        expires = timedelta(days=10)
        identities = user.email
        access_token = create_access_token(
            identity=identities, expires_delta=expires)

        return {'access_token': access_token}


class UserReset(Resource):

    def post(self):
        email = request.json['email']
        user = UsersModel.query.filter_by(email=email).first()
        if not user:
            return {'error': 'Not found email '}, 404
        expires = timedelta(hours=3)
        identities = email
        reset_token = create_access_token(
            identity=identities, expires_delta=expires)
        return {"message": "okey"}


class Userslist(Resource):
    @jwt_required
    def get(self):
        user_from_token = get_jwt_identity()
        user = UsersModel.query.filter_by(email=user_from_token).first()
        if user.is_Admin == True:
            users = UsersModel.query.all()
            result = users_schema.dump(users)
            return {"data": result}
        return{"error": "you don't have sufficient privileges to view all users please Contact Your Admin"}, 401

# *** get , delete,update a user


class UserResource(Resource):
    @jwt_required
    def get(self, user_id):
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(
            email=user_from_token).first()
        check_if_user_exists = UsersModel.query.get(user_id)
        if not check_if_user_exists:
            return {"message": "Not found User"}, 404
        if current_user.id == user_id:
            users = UsersModel.query.get(user_id)
            result = user_schema.dump(users)
            return jsonify(result=result)
        return {"error": " You Dont have previlege to view other users"}, 403

    @jwt_required
    def put(self, user_id):
        users = UsersModel.query.get(user_id)
        if not users:
            return {"message": "Not found User"}, 404
        fullName = request.json['fullName']
        userName = request.json['username']
        email = request.json['email']
        phoneNum = request.json['phoneNum']
        create_Admin = request.json['is_Admin']
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(
            email=user_from_token).first()
        if current_user.is_Admin == True:
            users.fullName = fullName
            users.userName = userName
            users.email = email
            users.phoneNum = phoneNum
            users.is_Admin = create_Admin
            db.session.commit()
            result = user_schema.dump(users)
            return jsonify(result)
        if current_user.id == user_id:
            users.fullName = fullName
            users.userName = userName
            users.email = email
            users.phoneNum = phoneNum
            db.session.commit()
            result = user_schema.dump(users)
            return jsonify(result=result)
        return {"error": " You Dont have previlege to update other users"}, 403

    @jwt_required
    def delete(self, user_id):
        users = UsersModel.query.get(user_id)
        if not users:
            return {"message": "Not found User"}, 404
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(
            email=user_from_token).first()
        if current_user.id == user_id:
            db.session.delete(users)
            db.session.commit()
            return{"message": " Successfully deleted."}, 200
        return {"error": " You Dont have previlege to delete other users"}, 403


class AuthUser(Resource):
    @jwt_required
    def get(self):
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(
            email=user_from_token).first()
        result = user_schema.dump(current_user)
        return jsonify(result=result)
