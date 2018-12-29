import logging

logging.basicConfig(level=logging.INFO)


def foo(s):
    # print('除数=%d'%s)                  #运行结果：除数=0
    # assert s!=0 ,'除数不能为0'          #运行结果：AssertionError: 除数不能为0
    return 10 / int(s)
    # # logging.basicConfig(level=logging.INFO)
    # logging.info('除数等于%s'%s)
def bar(s):
    return foo(s) * 2
def main():
    bar('0')
# def main():
#     foo(0)
main()
