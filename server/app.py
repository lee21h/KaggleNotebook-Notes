from datetime import datetime
from functools import total_ordering

from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///olotc.sqlite3'
app.config['SECRET_KEY'] = "random-secret-strong-string"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

class trade(db.Model):
    id = db.Column('entry_id', db.Integer, primary_key = True)
    datetime = db.Column(db.DateTime, nullable=False)
    price_usd = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    total_value = db.C