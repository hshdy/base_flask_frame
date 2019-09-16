# _*_coding:utf-8 _*_
# author: hsh
# file name: initialization.py
# data: 2019/8/26 15:01
from flask import Flask
from flask_restful import Api

from api.v1.index import Index
from logger.logger_service import logger


def init_base():
    # logger.info('start init base server')
    print('start init base server')
    # init_mysql()
    # init_mongo()

    # logger.info('finish base server')


def init_web_service():
    # logger.info('start init flask')

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Index, '/index')

    app.run("0.0.0.0",8888,debug=True)


def init():
    init_base()
    init_web_service()
