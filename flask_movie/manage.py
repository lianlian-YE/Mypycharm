from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager
from config import app
from getpass import getpass
from models import db, Admin
manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def createsuperuser():
    from werkzeug.security import generate_password_hash
    try:
        name=input('超级管理员名称：')
        passwd=getpass('超级管理员密码：')
        admin=Admin(name=name,passwd=generate_password_hash(passwd))
        db.session.add(admin)
        db.session.commit()
    except Exception:
        print('创建超级管理员失败！')
    else:
        print('创建超级管理员%s成功'%name)

if __name__=='__main__':
    manager.run()
