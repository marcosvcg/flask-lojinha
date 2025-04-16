from flask import Blueprint, jsonify, request
from services import ProductService
from util.exceptions import NotFoundError
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint('product', __name__, url_prefix='/products')

@bp.route('/', methods=['GET'])
def get_products():
    products = ProductService.get_all_products()
    return jsonify([product.to_dict() for product in products]), 200

@bp.route('/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        product = ProductService.get_product_by_id(product_id)
        return jsonify(product.to_dict()), 200
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404

@bp.route('/', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        product = ProductService.create_product(data)
        return jsonify(product.to_dict()), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.get_json()
        product = ProductService.update_product(product_id, data)
        return jsonify(product.to_dict()), 200
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        ProductService.delete_product(product_id)
        return '', 204
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404