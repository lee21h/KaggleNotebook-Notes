from datetime import datetime
from functools import total_ordering

from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_o