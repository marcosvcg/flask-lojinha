from models import Order
from util.database import db
from sqlalchemy.exc import SQLAlchemyError
from util.exceptions import NotFoundError

class OrderRepository:

    @staticmethod
    def add(data):
        try:
            order = Order(**data)
            db.session.add(order)
            db.session.commit()
            return order
        except:
            raise SQLAlchemyError

    @staticmethod
    def get_all():
        return Order.query.all()

    @staticmethod
    def get_by_id(order_id):
        order = Order.query.get(order_id)
        if not order:
            raise NotFoundError(f"Pedido com ID {order_id} não encontrado.")
        return order

    @staticmethod
    def delete(order_id):
        order = OrderRepository.get_by_id(order_id)
        db.session.delete(order)
        db.session.commit()

    @staticmethod
    def update(order_id, data):
        order = OrderRepository.get_by_id(order_id)
        for key, value in data.items():
            setattr(order, key, value)
        db.session.commit()
        return order