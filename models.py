from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Canidates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    past_experience = db.Column(db.Text, nullable=False)
    reason = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.Unicode(11))
    department = db.Column(db.String(120), nullable=False)
    year = db.Column(db.String(120), nullable=False)
    domain = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)
    remarks = db.Column(db.Text, nullable=False)
    remarks_by = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"User('{self.first_name}', '{self.email}', '{self.department}')"


class RegistrationControls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isRegistration = db.Column(db.Boolean, nullable=False)

    def __init__(self, isRegistration):
        self.isRegistration = isRegistration
