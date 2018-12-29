from flask import Flask,render_template
from flask_bootstrap import Bootstrap

app=Flask(__name__)
bootstrap=Bootstrap(app)
class testObj(object):
    def __init__(self, name):
        self.name = name
    def hello(self):
        return self.name
# @app.route('/test/')
# def test():
#     dict = {
#         'a': 'dict1',
#         'b': 'dict2'
#     }
#     list = ['l1', 'l2', 'l3']
#     var = 2
#     test=testObj('xiaoxinxin')
#     return render_template('test.html',dict=dict,list=list,var=var,test=test)
# @app.route('/')
# def testuser():
#     list=[1,2,3]
#     return render_template('test2.html',list=list)
# @app.route('/')
# def testmacro():
#     return render_template('test4.html')
# if __name__=='__main__':
#     app.run(port=5004)
print(bootstrap)