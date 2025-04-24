from util.database import db
from sqlalchemy.orm import relationship
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    order_date_only = db.Column(db.Date, nullable=False)
    order_time_only = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending') # Status ('pending', 'delivered')
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False)
    
    items = relationship('OrderItem', back_populates='order')
    address = relationship('Address', back_populates='orders')

    def to_dict(self):
        return {
            'id': self.id,
            'order_date': self.order_date_only.strftime("%d/%m/%Y"),
            'order_time': self.order_time_only.strftime("%H:%M:%S"),
            'status': self.status,
            'total_price': "R$" + str(self.total_price),
            'completed_at': self.completed_at.strftime("%d/%m/%Y - %H:%M:%S") if self.completed_at else None,
            'address': self.address.to_dict() if self.address else None,
            'items': [{
                    'order_item_id': item.id,
                    'product_quantity': item.product_quantity,
                    'product': {
                        'id': item.product.id,
                        'name': item.product.name,
                        'price': "R$" + str(item.product.price),
                        }
                } for item in self.items
            ]
        }