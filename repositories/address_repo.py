from models import Address
from util.database import db
from sqlalchemy.exc import SQLAlchemyError

class AddressRepository:
    
    @staticmethod
    def add(data):
        try:
            address = Address(**data)
            db.session.add(data)
            db.session.commit()
            return address
        execpt SQLAlchemyError as e:
        db.session.rollback()
        raise e