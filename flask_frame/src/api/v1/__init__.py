from api.v1.index import Index
from globals import GLOBAL


def loading_rout():
    api = GLOBAL.get_flask_api()
    api.add_resource(Index, '/index')