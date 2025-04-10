from flask import Blueprint, jsonify
from models import OrderItem

bp = Blueprint('order_item', __name__, url_prefix='/order_items')

@bp.route('/', methods=['GET'])
def get_order_items():
    order_items = OrderItem.query.all()
    return jsonify([item.to_dict() for item in order_items])