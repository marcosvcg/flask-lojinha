from repositories import AddressRepository
from sqlalchemy.exc import SQLAlchemyError

class AddressService:

    @staticmethod
    def create_address(data):
        try:
            address = AddressRepository.add(data)
            return address
        except SQLAlchemyError as e:
            return {"error": "Erro ao registrar endereço."}, 500

    @staticmethod
    def get_all_addresses():
        return AddressRepository.get_all()

    @staticmethod
    def get_address_by_id(address_id):
        return AddressRepository.get_by_id(address_id)

    @staticmethod
    def update_address(address_id, data):
        return AddressRepository.update(address_id, data)

    @staticmethod
    def delete_address(address_id):
        AddressRepository.delete(address_id)
        return {"message": f"Endereço removido com sucesso."}, 200