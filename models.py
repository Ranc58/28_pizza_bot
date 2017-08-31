from sqlalchemy import ForeignKey, Column, String, Text, Integer, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

BASE = declarative_base()

association_table = Table('association', BASE.metadata,
                          Column('pizzas_id', Integer,
                                 ForeignKey('pizzas.id')),
                          Column('pizza_variable_data_id', Integer,
                                 ForeignKey('pizza_variable_data.id')))


class Pizza(BASE):
    __tablename__ = 'pizzas'
    id = Column(Integer, primary_key=True)
    pizza_title = Column(String(128))
    pizza_toppings = Column(Text)
    pizza_variable_content = relationship('PizzaVariableData',
                                          secondary=association_table)


class PizzaVariableData(BASE):
    __tablename__ = 'pizza_variable_data'
    id = Column(Integer, primary_key=True)
    pizza_size = Column(String(64))
    pizza_price = Column(Integer)

    def __str__(self):
        return '{size} - {price}р.'.format(size=self.pizza_size,
                                           price=self.pizza_price)
