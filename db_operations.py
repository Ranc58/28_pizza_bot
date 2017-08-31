import argparse
import json
from os import getenv
from os.path import exists

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import BASE, Pizza, PizzaVariableData

PATH_TO_DB = getenv('PATH_TO_PIZZA_DB')
ENGINE = create_engine('sqlite:///{path_to_db}'.format(path_to_db=PATH_TO_DB),
                       echo=True)


def create_db():
    if not exists(PATH_TO_DB):
        BASE.metadata.create_all(ENGINE)


def load_catalog_from_json(json_file):
    return json.load(json_file)


def update_pizza_catalog(catalog):
    session = sessionmaker(bind=ENGINE)()
    for pizza in catalog:
        new_pizza = Pizza(**{'pizza_title': pizza['title'],
                             'pizza_toppings': pizza['description']})
        for choice in pizza['choices']:
            choices = PizzaVariableData(**{'pizza_size': choice['title'],
                                           'pizza_price': choice['price']})
            new_pizza.pizza_variable_content.append(choices)
        session.add(new_pizza)
    session.commit()


def create_parser_for_user_arguments():
    parser = argparse.ArgumentParser(description='Work with database.')
    parser.add_argument('-c', '--create', action='store_true',
                        help='Create database')
    parser.add_argument('-u', '--update', nargs='?', required=False,
                        type=argparse.FileType(mode='r'),
                        help='Update database')
    return parser.parse_args()


if __name__ == '__main__':
    user_argument = create_parser_for_user_arguments()
    if user_argument.create:
        create_db()
    else:
        pizza_catalog = load_catalog_from_json(user_argument.update)
        update_pizza_catalog(pizza_catalog)
