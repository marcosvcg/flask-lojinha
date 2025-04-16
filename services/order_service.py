from repositories import OrderRepository
from sqlalchemy.exc import SQLAlchemyError

class OrderService:

    @staticmethod
    def create_order(data):
        try:
            order = OrderRepository.add(data)
            return order
        except SQLAlchemyError:
            return {"error": "Erro ao registrar pedido."}, 500

    @staticmethod
    def get_all_orders():
        return OrderRepository.get_all()

    @staticmethod
    def get_order_by_id(order_id):
        return OrderRepository.get_by_id(order_id)

    @staticmethod
    def update_order(order_id, data):
        return OrderRepository.update(order_id, data)

    @staticmethod
    def delete_order(order_id):
        OrderRepository.delete(order_id)
        return {"message": "Pedido removido com sucesso."}, 200