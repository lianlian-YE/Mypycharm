"""

目标:
    模板引擎Jinja2的安装
    简单使用
    条件判断语句
    循环语句
    模板继承





1. 什么是模板?
    模板里面包含变量占位， 当模板的内容动态赋值后， 返回给用户; ==== 渲染


2. python里面自带的模板;（string模块提供）

缺点: 无法实现for循环， 判断语句和继承等;

    import  string

    # 常用的一些字符串变量
    # print(string.ascii_letters)
    # print(string.ascii_lowercase)
    # print(string.digits)
    # print(string.hexdigits)
    # print(string.octdigits)


    t1 = string.Template('$who is $role')
    print(t1.substitute(who="粉条", role="副总"))

"""

from flask import Flask, request, render_template, redirect, flash, abort

app = Flask(__name__)
users = ["user"+str(i+1) for i in range(100)]
d  = dict.fromkeys(users, '000000')

# 路由: http://ip:port
@app.route('/')
def index():
    # 传递后台的数据给前台html页面， 可以传递任意数据类型;（int, float, 对象, list........）
    return render_template('index_01.html', message="这是一个变量", li=[1, 2, 3, 4], d={'a': 1, 'b': 2})


@app.route('/list')
def list():
    # 通过表格方式显示用户名和密码;
    return  render_template('list.html', users = d, isVip= "True")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9004)
