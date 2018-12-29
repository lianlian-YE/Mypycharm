from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:yixin901213@localhost/flask_blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='True'
db=SQLAlchemy(app)
bootstrap=Bootstrap(app)
app.config['SECRET_KEY']='123456'

