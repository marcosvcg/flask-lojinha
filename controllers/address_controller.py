from flask import Blueprint, jsonify, request
from services import AddressService
from util.exceptions import NotFoundError
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint('address', __name__, url_prefix='/addresses')

@bp.route('/', methods=['GET'])
def get_addresses():
    addresses = AddressService.get_all_addresses()
    return jsonify([address.to_dict() for address in addresses]), 200


@bp.route('/<int:address_id>', methods=['GET'])
def get_address_by_id(address_id):
    try:
        address = AddressService.get_address_by_id(address_id)
        return jsonify(address.to_dict()), 200
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404


@bp.route('/', methods=['POST'])
def create_address():
    try:
        data = request.get_json()
        address = AddressService.create_address(data)
        return jsonify(address.to_dict()), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400


@bp.route('/<int:address_id>', methods=['PUT'])
def update_address(address_id):
    try:
        data = request.get_json()
        address = AddressService.update_address(address_id, data)
        return jsonify(address.to_dict()), 200
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400


@bp.route('/<int:address_id>', methods=['DELETE'])
def delete_address(address_id):
    try:
        AddressService.delete_address(address_id)
        return jsonify({'message': 'Endereço excluído com sucesso.'}), 204
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400