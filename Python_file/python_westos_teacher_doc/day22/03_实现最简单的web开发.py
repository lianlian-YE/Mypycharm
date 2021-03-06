"""
目标:
    Flask应用的基本构成?



"""

# 1. 导入Flask类;
from flask import Flask, render_template



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



@app.route('/westos/')
def westos():
    # 如何在flask程序中返回一个html页面;flask默认查找页面内容的位置为templates目录;
    return render_template('westos.html')



if __name__ == "__main__":
    # 4. 运行flask应用,
        # 默认端口是5000, 如果想要修改端口,传递参数port=xxx;
        # 默认情况下该web程序只能在本机浏览器访问, 如果想要其他主机访问, 指定host="0.0.0.0"
    app.run(host='0.0.0.0', port=9000)

