from util.database import db
from sqlalchemy.orm import relationship
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False, default='pending') # Status ('pending', 'delivered')
    total_price = db.Column(db.Float, nullable=False, default=0.0)
    completed_at = db.Column(db.DateTime, nullable=True)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False)
    
    items = relationship('OrderItem', back_populates='order')
    address = relationship('Address', back_populates='orders')

    def to_dict(self):
        return {
            'id': self.id,
            'order_date': self.order_date.isoformat(),
            'status': self.status,
            'total_price': self.total_price,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'address': self.address.to_dict() if self.address else None,
            'items': [item.to_dict() for item in self.items]
        }