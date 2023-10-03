from sqlalchemy import Boolean, Column,Integer,String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from Database import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50), unique=True)
    price = Column(Float)
    quantity = Column(Integer)
    description = Column(String(100))
    category = Column(String(50))


class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer,primary_key=True,index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    sale_date = Column(DateTime, default=datetime.utcnow)
    quantity_sold = Column(Integer)
    revenue = Column(Float)


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer,primary_key=True,index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    contact = Column(String(15), unique=True)
    Address = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    phone = Column(String(50), unique=True)


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15))
    address = Column(String(100))

