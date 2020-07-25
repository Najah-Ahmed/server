from flask import request, jsonify
from datetime import datetime

from flask_restful import Resource
from schema.feedback import feedback_schema, feedbacks_schema
from models.feedback import FeedbackModel
from models.user import UsersModel
from models.tickets import TicketModel
from db import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from schema.user import users_schema


class FeedbacksResource(Resource):
    @jwt_required
    def get(self, id):
        # user_from_token = get_jwt_identity()
        feedback = FeedbackModel.query.get(id)
        # current_user = UsersModel.query.filter_by(email=user_from_token).first()
        if not feedback:
            return {"message": "Not found User"}, 404
        # if current_user.id==feedback.owner_id:
        result = feedback_schema.dump(feedback)
        return jsonify(result)
        # # return {"message": "get single feedback {}".format(id)}
        # return {"error":" You Dont have previlege to view other users feedback"},403

    @jwt_required
    def put(self, id):
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(email=user_from_token).first()
        feed_back = FeedbackModel.query.get(id)
        if not feed_back:
          return {"message": "Not found Feeback"}, 404
        if current_user.id==feed_back.owner_id:
          comment = request.json['comment']
          rating = request.json['rating']
          feed_back.comment=comment
          feed_back.rating=rating
          db.session.commit()
          result = feedback_schema.dump(feed_back)
          return jsonify(result)
          
        return {"error":" You Dont have previlege to update other users feedback"},403

    @jwt_required
    def delete(self, id):
        user_from_token = get_jwt_identity()
        current_user = UsersModel.query.filter_by(email=user_from_token).first()
        feed_back = FeedbackModel.query.get(id)
        if not feed_back:
          return {"message": "Not found Feeback"}, 404
        if current_user.id==feed_back.owner_id:
          print(feed_back.owner_id)
          db.session.delete(feed_back)
          db.session.commit()
          return{"message": " Successfully deleted."}, 200
          
        return {"error":" You Dont have previlege to delete other users feedback"},403


class FeedbacksList(Resource):
    @jwt_required
    def get(self):
        feedback = FeedbackModel.query.all()
        result = feedbacks_schema.dump(feedback)
        return {"data": result}
      # return {"error":"there is no feedback belong to {user.email}".format(user.email)}
      

    # @jwt_required
    # def post(self):
    #     user_from_token = get_jwt_identity()
    #     # print(user_from_token)
    #     user = UsersModel.query.filter_by(email=user_from_token).first()
        
    #     comment = request.json['comment']
    #     rating= request.json['rating']
    #     user_id=user.id
    #     ticket_id=
    #     created_at = str(datetime.now())
    #     new_feedback=FeedbackModel(comment=comment, rating=rating,created_at=created_at,owner_id=user_id,ticket_id=ticket_id)
    #     db.session.add(new_feedback)
    #     db.session.commit()
    #     return {"message": "Thank You Saved !"}
      
class Feedbacks(Resource):
  @jwt_required
  def post(self,id):
    user_from_token = get_jwt_identity()
        # print(user_from_token)
    ticket_id=id
    user = UsersModel.query.filter_by(email=user_from_token).first()
    ticket = UsersModel.query.filter_by(id=ticket_id).first()
    if not ticket:
      return {'error': 'Not found ticket '}, 404
    
    comment = request.json['comment']
    rating= request.json['rating']
    user_id=user.id
    created_at = str(datetime.now())
    new_feedback=FeedbackModel(comment=comment, rating=rating,created_at=created_at,owner_id=user_id,ticket_id=ticket_id)
    db.session.add(new_feedback)
    db.session.commit()
    return {"message": "Thank You Saved !"}
    