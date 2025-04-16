from repositories import CategoryRepository
from sqlalchemy.exc import SQLAlchemyError

class CategoryService:

    @staticmethod
    def create_category(data):
        try:
            category = CategoryRepository.add(data)
            return category
        except SQLAlchemyError:
            return {"error": "Erro ao registrar categoria."}, 500

    @staticmethod
    def get_all_categories():
        return CategoryRepository.get_all()

    @staticmethod
    def get_category_by_id(category_id):
        return CategoryRepository.get_by_id(category_id)

    @staticmethod
    def update_category(category_id, data):
        return CategoryRepository.update(category_id, data)

    @staticmethod
    def delete_category(category_id):
        CategoryRepository.delete(category_id)
        return {"message": "Categoria removida com sucesso."}, 200