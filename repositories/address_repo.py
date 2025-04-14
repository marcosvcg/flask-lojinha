from models import Address
from util.database import db
from sqlalchemy.exc import SQLAlchemyError
from exceptions import NotFoundError

class AddressRepository:
    
    @staticmethod
    def add(data):
        try:
            address = Address(**data)
            db.session.add(address)
            db.session.commit()
            return address

    @staticmethod
    def get_all():
        return Address.query.all()

    @staticmethod
    def get_by_id(address_id):
        address = Address.query.get(address_id)
        if not address:
            raise NotFoundError(f"Endereço com ID {address_id} não encontrado.")
        return address

    @staticmethod
    def delete(address_id):
        address = AddressRepository.get_by_id(address_id)
        db.session.delete(address)
        db.session.commit()

    @staticmethod
    def update(address_id, data):
        address = AddressRepository.get_by_id(address_id)
        for key, value in data.items():
            setattr(address, key, value)
        db.session.commit()
        return address