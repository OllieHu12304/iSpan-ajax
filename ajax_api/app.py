from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
from routes.api import api_bp
from models import db # 從 models/__init__.py 匯入 db 物件
import os

# 建立 Flask 物件
app = Flask(__name__)

# 對 app 套用 CORS
CORS(app)


#將 Flask 應用程式轉成 RESTful API 的架構
api = Api(app)  



# 設定資料庫
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mydb.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 初始化
db.init_app(app)
          

# 好一點的架構
# 註冊 Blueprint
app.register_blueprint(api_bp, url_prefix='/api')



if __name__ == '__main__':
    app.run(debug=True)
