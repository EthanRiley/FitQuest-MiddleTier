from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

maxi = Blueprint('maxi', __name__)



