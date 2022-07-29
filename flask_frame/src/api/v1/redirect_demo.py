from flask import request
from flask_restful import Resource
from werkzeug.utils import redirect

from logger.logger_service import logger


class RedirectDemo(Resource):

    def get(self):
        logger.info("enter into RedirectDemo api.request method is {}".format(request.method))

        return redirect('http://www.baidu.com')
