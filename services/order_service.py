from repositories import OrderRepository
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, date, time

class OrderService:

    @staticmethod
    def create_order(data):
        validated_data = OrderService.validate_and_return_data(data)
        try:
            order = OrderRepository.add(validated_data)
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
    
    

# ---------------------------------------------------------------
    """   Métodos para validar a data e hora do pedido   """
# ---------------------------------------------------------------

    @staticmethod
    def validate_order_date(order_date):
        if isinstance(order_date, date):
            return order_date
        
        try:
            return datetime.strptime(order_date, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de data inválido. Use o formato DD/MM/YYYY.")

    @staticmethod
    def validate_order_time(order_time):
        if isinstance(order_time, time):
            return order_time
        
        try:
            return datetime.strptime(order_time, "%H:%M:%S").time()
        except ValueError:
            raise ValueError("Formato de hora inválido. Use o formato HH:MM:SS.")

    @staticmethod
    def validate_order_date_and_time(data):
        try:
            order_date = OrderService.validate_order_date(data['order_date'])
            order_time = OrderService.validate_order_time(data['order_time'])
        except ValueError as e:
            raise ValueError(str(e))
        return order_date, order_time

    @staticmethod
    def validate_and_return_data(data):
        order_date, order_time = OrderService.validate_order_date_and_time(data)
        return {
            'order_date': order_date,
            'order_time': order_time,
            'status': data['status'],
            'total_price': data['total_price'],
            'address_id': data['address_id']
        }