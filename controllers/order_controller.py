from flask import Blueprint, jsonify
from models import Order

bp = Blueprint('order', __name__, url_prefix='/orders')

@bp.route('/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])