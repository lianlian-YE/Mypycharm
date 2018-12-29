"""
目标:
    如何给html页面传递变量?
            render_templates("xxx.html", message ="xxxxx", code="xxx")


    如何显示给html传递的变量?
            {{ message }}


    # 404异常处理函数;@app.errorhandler(404)

    # 抛出异常: abort
"""

from flask import Flask, request, render_template, redirect, flash, abort

app = Flask(__name__)
users = {
    'root': 'redhat',
    'westos': 'westos'
}


# 路由: http://ip:port
@app.route('/')
def index():
    return render_template('index.html')


# 需要用到POST方法;
# 通过route装饰器传递methods参数, 可以改变HTTP的方法;
@app.route('/login', methods=['GET', 'POST'])
def login():
    # 1. 判断http方法, 如果是post;
    if request.method == 'POST':
        # 2. 获取前端用户表单提交的数据;
        username = request.form['name']
        passwd = request.form['passwd']

        # 3. 判断用户名和密码是否正确?
        if username in users:
            # 跳转到另外一个页面
            if passwd == users[username]:
                return redirect('https://www.baidu.com/')
            else:
                message = "用户密码错误"
                return render_template('login.html', message=message)
        else:
            message = "用户不存在, 请注册"
            return render_template('login.html', message=message)
    # 4. 如果不是post方法, 用户没有提交数据, 则进入登录界面;
    else:
        return render_template('login.html')


# 404异常处理函数;@app.errorhandler(404)
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


# 抛出异常: abort
@app.route('/users/<id>')
def user(id):
    if int(id) in range(1, 10):
        return "hello user" + str(id)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9003)
