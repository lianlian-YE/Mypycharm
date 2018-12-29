from flask import current_app
from flask_login import UserMixin
from flask_login._compat import unicode
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from configs import db, loginmanager, manager
from werkzeug.security import generate_password_hash,check_password_hash
class Permission:
    FOLLOW=0x01
    COMMENT=0x02
    WRITE_ARTICLES=0x04
    MODERATE_COMMENTS=0x08
    ADMINISTER=0x80
class User(UserMixin,db.Model):
    __tablename__='users'
    uid=db.Column(db.Integer,primary_key=True,autoincrement=True)
    uname=db.Column(db.String(50),unique=True)
    password_hash=db.Column(db.String(200))
    email=db.Column(db.String(64),unique=True,index=True)
    rold_id=db.Column(db.Integer,db.ForeignKey('roles.id'),default=1)
    confirmed=db.Column(db.Boolean,default=False)
    abc=db.Column(db.Integer)
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    @property
    def password(self):
        raise AttributeError('password is not readable attribute')
    @password.setter
    def password(self,password):
        # print()
        self.password_hash=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    def get_id(self):
        return unicode(self.uid)
    def generate_confirmation_token(self,expiration=3600):
        """
        生成令牌，有效期默认为一小时
        :param expiration:
        :return:
        """
        s=Serializer(current_app.config['SECRET_KEY'],expiration)   #TimedJSONWebSignatureSerializer生成具有过期时间的json web签名
        return s.dumps({'confirm':self.uid})    #为指定数据生成一个加密签名，然后对数据和签名进行序列化
    def confirm(self,token):
        """
        检验令牌，如果检验通过，confirmed属性设为True
        :param token:
        :return:
        """
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data=s.loads(token)
        except:
            return False
        if data.get('confirm')!=self.uid:
            return False
        self.confirmed=True
        db.session.add(self)
        return True

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True,unique=True)
    name=db.Column(db.String(64))
    default=db.Column(db.Boolean,default=False,index=True)
    permissions=db.Column(db.Integer)
    users=db.relationship('User',backref='role',lazy='dynamic')
    def __repr__(self):
        return "role %s" %(self.name)


    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES, True),
            'Moderator': (
            Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES | Permission.MODERATE_COMMENTS, True),
            'Administrator': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = role[r][0]
            role.default = role[r][1]
            db.session.add(role)
        db.session.commit()
@loginmanager.user_loader
def load_user(user_id):
    """
    flask-login要求程序实现一个回调函数，使用指定的标识符加载用户。
    加载用户的回调函数接收以Unicode字符串形式表示的用户标识符。
    如果能找到用户，这个函数必须返回用户对象，否则返回None
    :param user_id:
    :return:
    """
    return User.query.get(int(user_id))

if __name__=='__main__':
    db.create_all()
