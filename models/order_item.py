from util.database import db
from sqlalchemy.orm import relationship

class OrderItem(db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False, default=1)
    price_at_time_of_order = db.Column(db.Float, nullable=False)

    order = relationship('Order', back_populates='items')
    product = relationship('Product', back_populates='order_items')

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'product_id': self.product_id,
            'product_quantity': self.product_quantity,
            'price_at_time_of_order': self.price_at_time_of_order,
            'product': self.product.to_dict() if self.product else None
        }