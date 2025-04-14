from repositories import AddressRepository
from sqlalchemy.exc import SQLAlchemyError

class AddressService:

    @staticmethod
    def create_address(data):
        try:
            address = AddressRepository.add(data)
            return address.to_dict(), 201
        except SQLAlchemyError as e:
            return {"error": "Erro ao registrar endereço."}, 500

    @staticmethod
    def get_all_addresses():
        addresses = AddressRepository.get_all()
        return [address.to_dict() for address in addresses], 200

    @staticmethod
    def get_address_by_id(address_id):
        address = AddressRepository.get_by_id(address_id)
        return address.to_dict(), 200

    @staticmethod
    def update_address(address_id, data):
        address = AddressRepository.update(address_id, data)
        return address.to_dict(), 200

    @staticmethod
    def delete_address(address_id):
        AddressRepository.delete(address_id)
        return {"message": f"Endereço removido com sucesso."}, 200
