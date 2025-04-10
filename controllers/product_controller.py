from flask import Blueprint, jsonify
from models import Product

bp = Blueprint('product', __name__, url_prefix='/products')

@bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])