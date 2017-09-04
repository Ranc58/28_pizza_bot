from sqlalchemy import ForeignKey, Column, String, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

BASE = declarative_base()


class Pizza(BASE):
    __tablename__ = 'pizzas'
    pizza_id = Column(Integer, primary_key=True)
    pizza_title = Column(String(128))
    pizza_toppings = Column(Text)
    pizza_variable_data = relationship('PizzaVariableData')


class PizzaVariableData(BASE):
    __tablename__ = 'pizza_variable_data'
    content_id = Column(Integer, primary_key=True)
    parent_pizza_id = Column(Integer, ForeignKey('pizzas.pizza_id'))
    pizza_size = Column(String(64))
    pizza_price = Column(Integer)

    def __repr__(self):
        return '{size} - {price}р.'.format(size=self.pizza_size,
                                           price=self.pizza_price)
