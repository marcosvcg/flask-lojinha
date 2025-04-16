from repositories import ProductRepository
from sqlalchemy.exc import SQLAlchemyError

class ProductService:

    @staticmethod
    def create_product(data):
        try:
            product = ProductRepository.add(data)
            return product
        except SQLAlchemyError:
            return {"error": "Erro ao registrar produto."}, 500

    @staticmethod
    def get_all_products():
        return ProductRepository.get_all()

    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.get_by_id(product_id)

    @staticmethod
    def update_product(product_id, data):
        return ProductRepository.update(product_id, data)

    @staticmethod
    def delete_product(product_id):
        ProductRepository.delete(product_id)
        return {"message": "Produto removido com sucesso."}, 200