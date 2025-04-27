from flask import Blueprint,jsonify
from ..model.model import student
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    dict1 = {1:"name",2:"gender"}
    users = student.query.all()
    for user in users:
        print(user.toString())
    return jsonify(users)