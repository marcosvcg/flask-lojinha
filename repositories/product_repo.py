from models import Product
from util.database import db
from sqlalchemy.exc import SQLAlchemyError
from util.exceptions import NotFoundError

class ProductRepository:

    @staticmethod
    def add(data):
        try:
            product = Product(**data)
            db.session.add(product)
            db.session.commit()
            return product
        except:
            raise SQLAlchemyError

    @staticmethod
    def get_all():
        return Product.query.all()

    @staticmethod
    def get_by_id(product_id):
        product = Product.query.get(product_id)
        if not product:
            raise NotFoundError(f"Produto com ID {product_id} não encontrado.")
        return product

    @staticmethod
    def delete(product_id):
        product = ProductRepository.get_by_id(product_id)
        db.session.delete(product)
        db.session.commit()

    @staticmethod
    def update(product_id, data):
        product = ProductRepository.get_by_id(product_id)
        for key, value in data.items():
            setattr(product, key, value)
        db.session.commit()
        return product