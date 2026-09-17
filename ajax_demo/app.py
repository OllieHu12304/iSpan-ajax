from flask import Flask, render_template
from flask_restful import Api, Resource
from routes.api import api_bp
from models import db
import os

# 建立 Flask應用程式的物件
app = Flask(__name__)

# 將Flask物件傳入Api類別，建立API物件
api = Api(app)


# =====連線到Sqllite資料庫=====
# 取得 app.py 所在位置的實際路徑
basedir = os.path.abspath(os.path.dirname(__file__))

# 定義要連到 my.db sqllite 資料庫的連線字串
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mydb.db')

# 關掉一些監控功能，提升效能
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化資料庫連線
db.init_app(app)




# ======= Flask Start =========
# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template('index.html')

# http://127.0.0.1:5000/about
@app.route('/about')
def about():
    return render_template('about.html')

# ======= Flask End =========

# ======= Flask API Start =========

# # GET http://127.0.0.1:5000/hello
# class HelloWorld(Resource): # HelloWorld Class 就是 API
#     def get(self):
#         # todo...
#         return {'message':'Hello Restful API!!'}
    
#     def post(self):
#         pass
#     def put(self):
#         pass
#     def delete(self):
#         pass

# class Hello(Resource):
#     # HTTP GET
#     def get(self):
#         return {'message':'Hello !!'}
#     # HTTP POST
#     def post(self):
#         pass

# # API 的路由
# # http://127.0.0.1:5000/api
# api.add_resource(HelloWorld, '/api')
# # http://127.0.0.1:5000/hello
# api.add_resource(Hello,'/hello')

#註冊 Blueprint
# http://127.0.0.1:5000/api
app.register_blueprint(api_bp, url_prefix='/api')
# ======= Flask API End =========

if __name__ == '__main__':
    app.run(debug=True)
