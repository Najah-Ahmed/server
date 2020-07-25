from flask import Flask
from flask_restful import Api
from functools import wraps
from flask_jwt_extended import JWTManager
from flask_mail import Message


from resources.users import UserLogin, UserRegister, UserReset, UserResource, Userslist
from resources.tickets import TicketsList, TicketsResource
from resources.feedback import FeedbacksResource, Feedbacks
from resources.booking import BookingsList, BookingsResource
from resources.payment import PaymentsList, PaymentsResource
import config
app = Flask(__name__)


api = Api(app)
app.config.from_object('config')
jwt = JWTManager(app)


@app.before_request
def create_tables():
    db.create_all()
    print("tables are updateing or created")



# *** Endpoint/Routers
# *** start users endpoints
api.add_resource(Userslist, '/api/v1/users')
api.add_resource(UserResource, '/api/v1/user/<int:user_id>')
api.add_resource(UserRegister, '/api/v1/register')
api.add_resource(UserLogin, '/api/v1/login')
api.add_resource(UserReset, '/api/v1/resetpassword')
# *** end users endpoints

# # *** start tickets endpoints
api.add_resource(TicketsList, '/api/v1/tickets')
api.add_resource(TicketsResource, '/api/v1/ticket/<int:id>')
# # *** end tickets endpoints

# # *** start feedback endpoints
# api.add_resource(FeedbacksList, '/api/v1/feedback')
api.add_resource(FeedbacksResource, '/api/v1/feedback/<int:feedback_id>')
api.add_resource(Feedbacks, '/api/v1/ticket/<int:id>/feedback')

# # *** end feedback endpoints

# # *** start booking endpoints
# api.add_resource(BookingsList, '/api/v1/bookings?q=<string:arrived>/<string:destination>/<string:time>')
api.add_resource(BookingsList, '/api/v1/bookings/')
api.add_resource(BookingsResource, '/api/v1/booking/<int:booking_id>')
# # *** end booking endpoints

# # *** start payments endpoints
api.add_resource(PaymentsList, '/api/v1/payments')
api.add_resource(PaymentsResource, '/api/v1/payment/<int:trans_id>')
# # *** end payments endpoints

# ***running app
if __name__ == '__main__':
    from db import db
    from ma import ma
    from mail import mail
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    app.run(debug=True)
