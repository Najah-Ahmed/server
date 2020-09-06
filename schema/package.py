from db import db

from marshmallow import fields, Schema
from models.packages import PackagesModel
from models.user import UsersModel


class PackageSchema(Schema):
    # *** field like to show

    # class Meta:
    #      fields = ('comment', 'rating', 'owner_id','created_at')
    class Meta:
        model = UsersModel
        sqla_session = db.session

    sender_user_id = fields.Integer()
    # package_id = fields.Integer()
    receiver_to_user = fields.String()
    receiver_to_place = fields.String()
    receiver_phone_number = fields.String()
    descriptions = fields.String()
    price = fields.Float()
    receiver_confirm = fields.Boolean()
    created_at = fields.DateTime()


package_schema = PackageSchema()
packages_schema = PackageSchema(many=True)
