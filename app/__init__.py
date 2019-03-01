from flask import Flask 

app = Flask(__name__, instance_relative_config=True)
from app import views #importamos views para ejecutarlo siempre después de la instacia app

app.config.from_object('config')

