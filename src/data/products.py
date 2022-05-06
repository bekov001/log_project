import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Products(SqlAlchemyBase, SerializerMixin):
    """Таблица товаров в бд"""
    __tablename__ = 'products'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    code = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    weight = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    delivery_price = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    path_to_image = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    volume = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    delivery_type = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    amount = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
