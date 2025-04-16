from flask import Blueprint, jsonify, request
from services import CategoryService
from util.exceptions import NotFoundError
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint('category', __name__, url_prefix='/categories')

@bp.route('/', methods=['GET'])
def get_categories():
    categories = CategoryService.get_all_categories()
    return jsonify([category.to_dict() for category in categories]), 200

@bp.route('/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    try:
        category = CategoryService.get_category_by_id(category_id)
        return jsonify(category.to_dict()), 200
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404

@bp.route('/', methods=['POST'])
def create_category():
    try:
        data = request.get_json()
        category = CategoryService.create_category(data)
        return jsonify(category.to_dict()), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    try:
        data = request.get_json()
        category = CategoryService.update_category(category_id, data)
        return jsonify(category.to_dict()), 200
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        CategoryService.delete_category(category_id)
        return '', 204
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404