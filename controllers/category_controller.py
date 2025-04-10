from flask import Blueprint, jsonify
from models import Category

bp = Blueprint('category', __name__, url_prefix='/categories')

@bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])