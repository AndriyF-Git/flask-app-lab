from flask import Flask, request, redirect, url_for, current_app

 #Якщо instance_relative_config=True, цей метод буде шукати файл config.py у інстанс-папці
app = Flask(__name__, 
            # instance_relative_config=True
            )    # Construct an instance of Flask class for our webapp

# app.config.from_pyfile("config.py", silent=True)  
app.config.from_object("config")

from config import config
app.config.from_object(config.get("testing"))  # Використання конфігурації для розробки


from . import views
from .commands import cli_bp
from .bpcookie import cook_bp as cook
app.register_blueprint(cli_bp)
app.register_blueprint(cook) 

