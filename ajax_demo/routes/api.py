from flask import Blueprint
from flask_restful import Api
from resources.items_api import Item, Items

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#設定路由
# http://127.0.0.1:5000/api/items/12
api.add_resource(Item, '/items/<int:id>')
# http://127.0.0.1:5000/api/items
api.add_resource(Items,'/items')
