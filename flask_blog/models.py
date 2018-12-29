from config import db


class User(db.Model):
    __tablename__ = 'User'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50),unique=True)
    passwd=db.Column(db.String(500))
    def __repr__(self):
        return self.username
db.create_all()