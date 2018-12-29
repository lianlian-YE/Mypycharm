"""

HTTP方法:
    告知服务器， 客户端想请求页面做什么?


    GET:浏览器告知服务器, 获取页面的内容， 返回给浏览器;
    POST:浏览器告诉服务器, 通常用于表单的提交;






"""

from flask import Flask, request, render_template, redirect

app = Flask(__name__)
users = {
    'root': 'redhat',
    'westos': 'westos'
}


# 路由: http://ip:port
@app.route('/')
def index():
    return render_template('index.html')


# 基本路由之传递参数;
# http://127.0.0.1:90002/user/2
@app.route('/user/<id>')
def userinfo(id):
    return "hello user" + str(id)


# 基本路由之从浏览器的请求中获取参数
@app.route('/query_user')
def query():
    # http://ip:port/query?id=12
    # 从字典中， 获取id对应的value值；
    id = request.args.get('id')
    return '查询用户： user' + str(id)


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
                return "用户密码错误"
        else:
            return render_template('login.html')

    # 4. 如果不是post方法, 用户没有提交数据, 则进入登录界面;
    else:
        return render_template('login.html')


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        # 2. 获取前端用户表单提交的数据;
        addName = request.form['name']
        addPasswd = request.form['passwd']

        # 3. 判断用户是否存在, 如果存在, 跳转到添加页面, 如果不存在, 则返回添加成功;
        if addName in users:
            return "用户已经存在, 不能添加"
        else:
            users[addName] = addPasswd
            return "用户%s添加成功" % (addName)
    return render_template('add.html')


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    # 删除子典的key-value值； del 字典名称[key]
    if request.method == 'POST':
        # 2. 获取前端用户表单提交的数据;
        delName = request.form['name']
        delPasswd = request.form['passwd']

        # 3. 判断用户是否存在, 如果存在, 跳转到添加页面, 如果不存在, 则返回添加成功;
        if delName in users:
            del  users[delName]
            return   "用户删除成功!"
        else:
            return "%s用户不存在" % (delName)
    return render_template('delete.html')





#
# @app.route('/list')
# def list():
#     """列出所有的用户和用户密码， 并以表格的方式显示"""
#     pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9002)
