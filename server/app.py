from datetime import datetime
from functools import total_ordering

from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///olotc.sql