from api.v1.handler_mysql_demo import HandlerMysqlDemo
from api.v1.index import Index
from api.v1.redirect_demo import RedirectDemo
from globals import GLOBAL


def loading_rout():
    api = GLOBAL.get_flask_api()
    api.add_resource(Index, '/')
    api.add_resource(HandlerMysqlDemo, '/mysql_demo')
    api.add_resource(RedirectDemo, '/redirect_demo')