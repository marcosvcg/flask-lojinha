from models import OrderItem
from util.database import db
from sqlalchemy.exc import SQLAlchemyError
from util.exceptions import NotFoundError

class OrderItemRepository:

    @staticmethod
    def add(data):
        try:
            item = OrderItem(**data)
            db.session.add(item)
            db.session.commit()
            return item
        except:
            raise SQLAlchemyError

    @staticmethod
    def get_all():
        return OrderItem.query.all()

    @staticmethod
    def get_by_id(item_id):
        item = OrderItem.query.get(item_id)
        if not item:
            raise NotFoundError(f"Item do pedido com ID {item_id} não encontrado.")
        return item

    @staticmethod
    def delete(item_id):
        item = OrderItemRepository.get_by_id(item_id)
        db.session.delete(item)
        db.session.commit()

    @staticmethod
    def update(item_id, data):
        item = OrderItemRepository.get_by_id(item_id)
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return item