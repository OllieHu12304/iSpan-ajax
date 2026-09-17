from flask_sqlalchemy import SQLAlchemy

# 建立 SqlAlchemy 物件，後續就會用這個物件提供的功能來操作資料庫
db = SQLAlchemy()

#匯入所有模型
from .user_model import User