import config

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref

engine = create_engine(config.DB_URI, echo = True) 
session = scoped_session(sessionmaker(bind = engine,
                                      autocommit = False,
                                      autoflush = False))

#required for SQLAlchemy's magic to work
Base = declarative_base()
Base.query = session.query_property()

#begin class declarations
class Customer(Base):
    #instances of this class will be stored in a table named "customers"
    __tablename__ = 'customers'
    id = Column(Integer, primary_key = True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    phonenumber = Column(String(20))
    email = Column(String(120))
2
class Delivery_Recipient(Base):
    __tablename__ = 'recipients'
    id = Column(Integer, primary_key = True)
    customer_id = Column(Integer, ForeignKey("customers.id")) #ForeignKey references a column in another table
    altname = Column(String(100), nullable = True) #nullable=True means that this column is optional
    altphonenumber = Column(String(20), nullable = True)
    companyname = Column(String(20), nullable = True)
    streetaddress = Column(String(100))
    unit = Column(String(20), nullable = True)
    city = Column(String(100))
    state = Column(String(20))
    zipcode = Column(String(20))
    customer = relationship("Customer", backref = backref("customer")) #establishes a relationship between the Delivery_Recipients and Customer objects

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key = True)
    flavor = Column(String(100))
    size = Column(String(50))
    cost = Column(Integer)
    quantity = Column(String(50))
    description = Column(String(200))

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key = True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    recipients_id = Column(Integer, ForeignKey("recipients.id"))
    date_time = Column(DateTime(20))
    delivery = Column(Boolean, default = False)
    decorationtheme = Column(String(100))
    colorscheme = Column(String(100))
    customer = relationship("Customer", backref = backref("orders", order_by=id))
    recipients = relationship("Delivery_Recipient", backref = backref("orders", order_by=id))

class Order_Product(Base):
    __tablename__ = 'orders_products'
    id = Column(Integer, primary_key = True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    order = relationship("Order", backref = backref("products", order_by=id))
    product = relationship("Product", backref = backref("orders", order_by=id))
#end class declarations

def create_tables(Base):
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables(Base)























