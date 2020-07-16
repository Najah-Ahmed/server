from db import db
# **** FeedbackModels


class FeedbackModel(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    rating = db.Column(db.Float)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'))
    created_at = db.Column(db.DateTime)

    def __init__(self, comment, rating, created_at,owner_id ,ticket_id):
        self.comment = comment
        self.rating = rating
        self.owner_id = owner_id
        self.ticket_id = ticket_id
        self.created_at = created_at
