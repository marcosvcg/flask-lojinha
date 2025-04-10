from flask import Blueprint, jsonify
from models import Address

bp = Blueprint('address', __name__, url_prefix='/addresses')

@bp.route('/', methods=['GET'])
def get_addresses():
    addresses = Address.query.all()
    return jsonify([address.to_dict() for address in addresses])
