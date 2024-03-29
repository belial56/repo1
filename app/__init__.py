from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

import views, models

import os
from flask_login import LoginManager
from config import basedir

#lm = LoginManager()
#lm.init_app(app)
