
from ma import ma
from models.payment import PaymentModel


class PaymentSchema(ma.Schema):
    # *** field like to show
    model = PaymentModel

    class Meta:
        fields = ('user_id',  'booking_id', 'amount',
                  'fullname', 'method_of_pay', 'created_at')


payment_schema = PaymentSchema()
payments_schema = PaymentSchema(many=True)
