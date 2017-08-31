from os import getenv
from flask import Flask, Response, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import Session
from werkzeug.exceptions import HTTPException

from db_operations import ENGINE
from models import Pizza, PizzaVariableData

LOGIN = getenv('PIZZA_ADMIN_PAGE_LOGIN')
PASSWORD = getenv('PIZZA_ADMIN_PAGE_PASSWORD')
SECRET_KEY = getenv('PIZZA_ADMIN_PAGE_SECRET_KEY')
app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            'Could not verify your access level for that URL.\n'
            'You have to login with proper credentials', 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}))


class PizzaModelView(ModelView):
    def check_auth(self, username, password):
        return username == LOGIN and password == PASSWORD

    def is_accessible(self):
        auth = request.authorization
        if not auth or not self.check_auth(auth.username, auth.password):
            raise AuthException('Not authenticated.')
        return True


session = Session(ENGINE)
admin = Admin(app, name='Pizza menu',
              template_mode='bootstrap3')
admin.add_view(PizzaModelView(Pizza, session))
admin.add_view(PizzaModelView(PizzaVariableData, session))

app.run()
