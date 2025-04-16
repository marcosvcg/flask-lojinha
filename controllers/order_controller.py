from flask import Blueprint, jsonify, request
from services import OrderService
from util.exceptions import NotFoundError
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint('order', __name__, url_prefix='/orders')

@bp.route('/', methods=['GET'])
def get_orders():
    orders = OrderService.get_all_orders()
    return jsonify([order.to_dict() for order in orders]), 200

@bp.route('/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    try:
        order = OrderService.get_order_by_id(order_id)
        return jsonify(order.to_dict()), 200
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404

@bp.route('/', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        order = OrderService.create_order(data)
        return jsonify(order.to_dict()), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        data = request.get_json()
        order = OrderService.update_order(order_id, data)
        return jsonify(order.to_dict()), 200
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        OrderService.delete_order(order_id)
        return '', 204
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404