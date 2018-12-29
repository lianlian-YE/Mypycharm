from flask import render_template
from configs import app
from auth.view import authbp
from flask_login import login_required

app.register_blueprint(authbp,url_prefix='/auth/')
@app.route('/secret/')
@login_required
def secret():
    """
    flask-login提供了login-required装饰器，保护路由只让认证用户访问。
    未认证用户访问时，会拦截请求，将用户发往登录页面。
    :return:
    """
    return 'only authenticated users are allowed!'
@app.route('/index/')
def index():
    return render_template('index.html')


if __name__ == '__main__':

    app.run('127.0.0.1','5001')


