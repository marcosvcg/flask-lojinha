from repositories import OrderItemRepository
from sqlalchemy.exc import SQLAlchemyError

class OrderItemService:

    @staticmethod
    def create_order_item(data):
        try:
            item = OrderItemRepository.add(data)
            return item
        except SQLAlchemyError:
            return {"error": "Erro ao registrar item do pedido."}, 500

    @staticmethod
    def get_all_order_items():
        return OrderItemRepository.get_all()

    @staticmethod
    def get_order_item_by_id(order_item_id):
        return OrderItemRepository.get_by_id(order_item_id)

    @staticmethod
    def update_order_item(order_item_id, data):
        return OrderItemRepository.update(order_item_id, data)

    @staticmethod
    def delete_order_item(order_item_id):
        OrderItemRepository.delete(order_item_id)
        return {"message": "Item do pedido removido com sucesso."}, 200