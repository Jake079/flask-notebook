from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
import pytz


def get_time():
    get_time_now = datetime.now(pytz.timezone('America/Chicago'))
    return get_time_now


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    note_data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=get_time)

    def formatted_time(self):
        return self.date.strftime('%Y-%m-%d %H:%M (CT/UTC-6)')


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
    notes = db.relationship('Note')
