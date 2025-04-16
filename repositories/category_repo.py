from models import Category
from util.database import db
from sqlalchemy.exc import SQLAlchemyError
from util.exceptions import NotFoundError

class CategoryRepository:

    @staticmethod
    def add(data):
        try:
            category = Category(**data)
            db.session.add(category)
            db.session.commit()
            return category
        except:
            raise SQLAlchemyError

    @staticmethod
    def get_all():
        return Category.query.all()

    @staticmethod
    def get_by_id(category_id):
        category = Category.query.get(category_id)
        if not category:
            raise NotFoundError(f"Categoria com ID {category_id} não encontrada.")
        return category

    @staticmethod
    def delete(category_id):
        category = CategoryRepository.get_by_id(category_id)
        db.session.delete(category)
        db.session.commit()

    @staticmethod
    def update(category_id, data):
        category = CategoryRepository.get_by_id(category_id)
        for key, value in data.items():
            setattr(category, key, value)
        db.session.commit()
        return category