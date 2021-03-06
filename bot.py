import telebot
from jinja2 import Template
from os import getenv
from sqlalchemy.orm import sessionmaker, joinedload
from db_operations import ENGINE
from models import Pizza

TOKEN = getenv('PIZZA_BOT_TOKEN')


if not TOKEN:
    raise Exception('BOT_TOKEN should be specified')

bot = telebot.TeleBot(TOKEN)

with open('templates/catalog.md', 'r') as catalog_file:
    catalog_tmpl = Template(catalog_file.read())

with open('templates/greetings.md', 'r') as greetings_file:
    greetings_tmpl = Template(greetings_file.read())


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, greetings_tmpl.render())


@bot.message_handler(commands=['menu'])
def show_catalog(message):
    session = sessionmaker(bind=ENGINE)()
    catalog = session.query(Pizza).options(joinedload('pizza_variable_data'))
    bot.send_message(message.chat.id,
                     catalog_tmpl.render(catalog=catalog.all()),
                     parse_mode='Markdown')


if __name__ == '__main__':
    bot.polling(none_stop=True)
