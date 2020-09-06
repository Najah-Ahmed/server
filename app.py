from flask_cors import CORS, cross_origin
from flask import Flask
from flask_restful import Api
from functools import wraps
from flask_jwt_extended import JWTManager
from flask_mail import Message


from resources.users import UserLogin, UserRegister, UserReset, UserResource, Userslist, AuthUser, VerifyEmailUser, ConformToken
from resources.tickets import TicketsList, TicketsResource
from resources.feedback import FeedbacksResource, Feedbacks, FeedbacksList, SingleUserFeedback
from resources.booking import SearchTicket, BookingsResource, BookingTicket, BookingList, SingleUserBooking
from resources.payment import PaymentsList,  PaymentBooking, PaymentPacakage, SingleUserPayment
from resources.package import PackageList, PackagesResources, SingleUserPackages
import config
import myToken
app = Flask(__name__)

api = Api(app)
app.config.from_object('config')
jwt = JWTManager(app)
CORS(app)


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
api.add_resource(AuthUser, '/api/v1/authuser')
api.add_resource(VerifyEmailUser, '/api/v1/sentemail')
api.add_resource(ConformToken, '/api/v1/confirm/<string:token>')
# *** end users endpoints

# # *** start tickets endpoints
api.add_resource(TicketsList, '/api/v1/tickets')
api.add_resource(TicketsResource, '/api/v1/ticket/<int:id>')
# # *** end tickets endpoints

# # *** start feedback endpoints
api.add_resource(FeedbacksList, '/api/v1/feedback')
api.add_resource(SingleUserFeedback, '/api/v1/userfeedback')
api.add_resource(FeedbacksResource, '/api/v1/feedback/<int:feedback_id>')
api.add_resource(Feedbacks, '/api/v1/ticket/<int:id>/feedback')

# # *** end feedback endpoints

# # *** start booking endpoints
api.add_resource(SearchTicket, '/api/v1/bookings/')
api.add_resource(BookingList, '/api/v1/booking/')
api.add_resource(SingleUserBooking, '/api/v1/userbooking/')
api.add_resource(BookingsResource, '/api/v1/booking/<int:booking_id>')
api.add_resource(BookingTicket, '/api/v1/bookingticket/<int:ticket_id>')
# # *** end booking endpoints

# # *** start payments endpoints
api.add_resource(PaymentsList, '/api/v1/payments')
api.add_resource(SingleUserPayment, '/api/v1/payment')
api.add_resource(PaymentBooking, '/api/v1/bookingpayment/<int:booking_id>')
api.add_resource(PaymentPacakage, '/api/v1/packagepayment/<int:package_id>')
# # *** end payments endpoints

# # *** start payments endpoints
api.add_resource(PackageList, '/api/v1/packages')
api.add_resource(SingleUserPackages, '/api/v1/userpackages')
api.add_resource(PackagesResources, '/api/v1/package/<int:package_id>')
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
