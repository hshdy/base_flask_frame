# _*_coding:utf-8 _*_
# author: hsh
# file name: index.py
# data: 2019/8/26 15:18
from flask_restful import Resource


class Index(Resource):

    def get(self):
        # logger('enter into index view function')
        print('enter into index view function')
        return 'index page'
