from ma import ma
from models.booking import BookingModel


class BookingSchema(ma.Schema):
    # *** field like to show
    model = BookingModel

    class Meta:
        fields = ('user_id', 'ticket_id', 'price', 'seat_no', 'created_at')


booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)
