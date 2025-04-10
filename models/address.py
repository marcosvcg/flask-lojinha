from util.database import db
from sqlalchemy.orm import relationship

class Address(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    postcode = db.Column(db.String(10), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(10), nullable=False)

    orders = relationship('Order', back_populates='address')

    def to_dict(self):
        return {
            'postcode': self.postcode,
            'state': self.state,
            'city': self.city,
            'street': self.street,
            'number': self.number
        }