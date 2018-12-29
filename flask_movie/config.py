from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:yixin901213@localhost:3306/flask_movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']='xiaoxinxin'
db=SQLAlchemy(app)
bootstrap=Bootstrap(app)




