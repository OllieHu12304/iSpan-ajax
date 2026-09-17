from . import db

class User(db.Model):
    __tablename__ = 'users'  #資料表名稱

    UserId = db.Column(db.Integer, primary_key=True)
    UserName= db.Column(db.Text)
    UserEmail = db.Column(db.Text)
    UserAge = db.Column(db.Integer)