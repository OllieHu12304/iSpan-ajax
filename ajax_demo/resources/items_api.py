from flask_restful import Resource
from models.user_model import User

class Items(Resource):
    def get(self):
        users = User.query.all() #讀取Users資料表中的所有資料 select * from users

        return [{
            "UserName": u.UserName,
            "UserEmail": u.UserEmail
            } for u in users],200


        # return {'message': f'讀取所有資料'}, 200

    def post(self):
        return {'message': f'新增資料'}, 201

class Item(Resource):
    def get(self, id):
        return {'message': f'根據{id}讀取資料'}, 200

    def put(self, id):
        return {'message': f'根據{id}修改資料'},200

    def delete(self, id):
        return {'message': f'根據{id}刪除資料'}, 200

   