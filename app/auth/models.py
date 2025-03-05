# models/user.py
from app import db,app
from datetime import datetime
from enum import Enum


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/bookingsystem?charset=utf8'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# db = SQLAlchemy(app)

class UserStatus(Enum):
    Student = 'Student'
    Teacher = 'Teacher'
    Admin = 'Admin'

class User(db.Model):
    
    __tablename__ = 'User'
    
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Enum(UserStatus), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    salt = db.Column(db.String(10), nullable=False)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)
    isDeleted = not db.Column(db.Boolean, default=False)  # in db is 0 or 1, 0 represents exist

    def __init__(self, status, name, email, password_hash, salt):
        self.status = status
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.salt = salt

@app.route('/')
def index():
    list_usrs = User.query.all()
    for usr in list_usrs:
        print(usr.name, 
              usr.email, 
              usr.status, 
              usr.createdAt, 
              usr.updatedAt, 
              usr.isDeleted
              )
    return 'hello world'
        
# if __name__ == '__main__':
    
#     app.run(debug=True)



