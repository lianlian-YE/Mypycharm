from datetime import datetime

from config import db

class Tag(db.Model):
    __tablename__='tag'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50),unique=True)
    add_time=db.Column(db.DateTime,default=datetime.now())
    movies=db.relationship('Movies',backref='tag')
    def __repr__(self):
        return 'Tag: %s'%self.name
class Movies(db.Model):
    __tablename__='Movies'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(50),unique=True)
    add_time=db.Column(db.DateTime,default=datetime.now())
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    url=db.Column(db.String(255),unique=True) #电影存放位置
    info=db.Column(db.Text)  #电影简介
    logo=db.Column(db.String(255),unique=True)  #电影封面
    area = db.Column(db.String(50))  # 地区
    length = db.Column(db.Integer)  # 片长
    release_time = db.Column(db.Date)  # 上映时间
    star = db.Column(db.SmallInteger)  # 星级
    def __repr__(self):
        return "<Movie %s>" % (self.title)

#管理员相关#############################################
class Admin(db.Model):
    """
    管理员类
    """
    __tablename__='admin'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50),unique=True)
    passwd=db.Column(db.String(100))
    add_time=db.Column(db.DateTime,default=datetime.now())
    adminlogs=db.relationship('AdminLog',backref='admin')
    def __repr__(self):
        return 'Admin:%s'%self.name
class AdminLog(db.Model):
    """
    管理员日志
    关系：管理员1——>日志n
    """
    __tablename__='AdminLog'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id=db.Column(db.Integer,db.ForeignKey('admin.id'))
    ip=db.Column(db.String(100))
    add_time=db.Column(db.DateTime,default=datetime.now())
    def __repr__(self):
        return 'ip:%s'%(self.ip)
class opLog(db.Model):
    """
    操作日志
    关系：管理员1——>操作日志n
    """
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(100))
    option=db.Column(db.String(50))
    add_time=db.Column(db.DateTime,default=datetime.now())

    def __repr__(self):
        return 'oplog:%s'%self.option