from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager
from . import config
from .utils import current_time
import base64


@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()


class User(db.Document, UserMixin):
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)

    # Returns unique string identifying our object
    def get_id(self):
        return self.username


class Schedule(db.Document):
    traveller = db.ReferenceField(User, required=True)
    originplace = db.StringField(required=True, min_length=3, max_length=3)
    destinationplace = db.StringField(
        required=True, min_length=3, max_length=3)
    departure_date = db.StringField(required=True)
    price = db.StringField(required=True)
