from flask import Blueprint, jsonify, request
from services import OrderItemService
from util.exceptions import NotFoundError
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint('order_item', __name__, url_prefix='/order_items')

@bp.route('/', methods=['GET'])
def get_order_items():
    items = OrderItemService.get_all_order_items()
    return jsonify([item.to_dict() for item in items]), 200

@bp.route('/<int:item_id>', methods=['GET'])
def get_order_item_by_id(item_id):
    try:
        item = OrderItemService.get_order_item_by_id(item_id)
        return jsonify(item.to_dict()), 200
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404

@bp.route('/', methods=['POST'])
def create_order_item():
    try:
        data = request.get_json()
        item = OrderItemService.create_order_item(data)
        return jsonify(item.to_dict()), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/<int:item_id>', methods=['PUT'])
def update_order_item(item_id):
    try:
        data = request.get_json()
        item = OrderItemService.update_order_item(item_id, data)
        return jsonify(item.to_dict()), 200
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/<int:item_id>', methods=['DELETE'])
def delete_order_item(item_id):
    try:
        OrderItemService.delete_order_item(item_id)
        return '', 204
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404