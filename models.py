from . import db
from datetime import date

class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, default=date.today, nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(250), default="")
    date = db.Column(db.Date, default=date.today, nullable=False)

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    target = db.Column(db.Float, nullable=False)
    saved = db.Column(db.Float, default=0)
    deadline = db.Column(db.Date, nullable=True)
