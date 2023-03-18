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
    total_value = db.Column(db.Float, nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, datetime, price_usd, quantity, total_value):
        self.datetime = datetime
        self.price_usd = float(price_usd)
        self.quantity = float(quantity)
        self.total_value = total_value


@app.route('/', methods=['GET'])
@cross_origin()
def get_all_trades():
    trades = trade.query.order_by(trade.datetime).all()
    output = []
    for t in trades:
        trade_data = {'datetime': t.datetime.strftime('%Y-%m-%dT%H:%M:%S.%fZ'), 'price_usd': t.price_usd, 'quantity': t.quantity, 'total_value': t.total_value}
        output.append(trade_data)
    return jsonify(output)

@app.route('/new', methods = ['POST'])
@