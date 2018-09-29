# -*- coding:utf-8 -*-
# class Config(object):
#     # 设置秘钥要没有规律

import os
BASE_DIR=os.path.abspath(os.path.dirname(__file__))
class Config(object):
    # 格式为mysql + pymysql://数据库用户名:密码@数据库地址:端口号/数据库的名字？数据库格式
    SECRET_KEY = 'a9087FFJFF9nnvc2@#$%FSD'
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@localhost:3306/flaskblog?charset=utf8'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

