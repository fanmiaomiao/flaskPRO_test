# -*- coding:utf-8 -*-
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)  #创建app应用，__name__是python预定义变量，被设置为本模块

app.config.from_object(Config)

# 建立数据库关系
db = SQLAlchemy(app)
# 绑定app和数据库，以便进行操作
migrate = Migrate(app,db)

login = LoginManager(app)

login.login_view = 'login'

from app import routes,models



