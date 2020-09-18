
from ma import ma
from models.payment import PaymentModel


class PaymentSchema(ma.Schema):
    # *** field like to show
    model = PaymentModel

    class Meta:
        fields = ('id', 'user_id',  'booking_id', 'amount', 'package_id',
                  'fullname', 'phoneNum', 'method_of_pay', 'created_at')


payment_schema = PaymentSchema()
payments_schema = PaymentSchema(many=True)
