
# 1. 导入Flask类;
from flask import Flask, render_template, request, url_for



# 2. 实例化Flaks类。 生成一个实例;
#       __name__结果是__main__或者模块名/包名, 根据这个参数确定项目的位置,（确定该项目的静态文件或者模板的位置）;
app = Flask(__name__)


# 3. 通过路由绑定处理的视图函数;
    # URL： （eg:http://127.0.0.1:5000/ ）
    # 装饰器@app.route()告诉Flask哪个url才能触发装饰器装饰的函数, 这个又专业的称为路由;
    # 定义的函数hello, return后面的返回值是想要显示在浏览器上的内容;
@app.route('/')
def hello():
    return "<h1 style='color:red'>hello python!</h1><br/><a href='/westos/'>西部开源技术中心</a>"


# 基本路由
@app.route('/westos/')
def westos():
    # 如何在flask程序中返回一个html页面;flask默认查找页面内容的位置为templates目录;
    return render_template('westos.html')



# 基本路由之传递参数;
@app.route('/user/<id>')
def userinfo(id):
    return "hello user" + str(id)


# 基本路由之从浏览器的请求中获取参数
@app.route('/query_user/')
def query():

    # http://ip:port/query?id=12
    # 从字典中， 获取id对应的value值；
    id = request.args.get('id')
    return '查询用户： user'+ str(id)





# 反向路由
@app.route('/query_url')
def query_url():
    """通过函数， 找到该函数对应的url地址;"""
    return  "查询的url地址为:" + url_for("query")




if __name__ == "__main__":
    # 4. 运行flask应用,
        # 默认端口是5000, 如果想要修改端口,传递参数port=xxx;
        # 默认情况下该web程序只能在本机浏览器访问, 如果想要其他主机访问, 指定host="0.0.0.0"
    app.run(host='0.0.0.0', port=9001)

