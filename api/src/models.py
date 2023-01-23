"""Models to database"""
from datetime import datetime
from api.src.utils import random_string
from app import db


class Provider(db.Model):
    """""Provider model"""
    __tablename__ = "providers"

    id = db.Column(db.String(16), primary_key=True, default=random_string)
    name = db.Column(db.String(50), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount_products = db.Column(db.Integer, nullable=False, default=0)

    def insert(self):
        """Insert data from Provider on database"""
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_id(cls, _id: str):
        """"Find Provider by id"""
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def update(cls, update, **kwargs):
        """Update data on database from Provider"""
        return cls.__commit(cls.query.filter_by(**kwargs).update(update))

    @classmethod
    def delete(cls, **kwargs):
        """Delete object Provider on database"""
        return cls.__commit(cls.query.filter_by(**kwargs).delete())

    @staticmethod
    def __commit(result: bool = False) -> bool:
        """"Commit data on database"""
        if result:
            db.session.commit()
            return True
        return False

    def __repr__(self):
        """"Representation from self"""
        return f"Provider: {self.id} - {self.name}/{self.company} - {self.amount_products} - {self.created_at}"
