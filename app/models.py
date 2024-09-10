import sqlalchemy as sa
from . import db

class User(db.Model):
    __tablename__ = "user"
    email = sa.Column(sa.String(length=50), primary_key=True)
    username = sa.Column(sa.String(length=20))
    password = sa.Column(sa.String(length=20))

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    domain = db.Column(db.String(100))
    year_founded = db.Column(db.Integer)
    industry = db.Column(db.String(50))
    size_range = db.Column(db.String(20))
    locality = db.Column(db.String(100))
    country = db.Column(db.String(100))
    linkedin_url = db.Column(db.String(200))
    current_employee_estimate = db.Column(db.Integer)
    total_employee_estimate = db.Column(db.Integer)