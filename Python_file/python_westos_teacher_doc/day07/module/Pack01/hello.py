a=10


def add(x,y):
    return x+y

# __name__如果不是导入的模块执行， 结果为__main__;
# __name__如果时被导入的模块， 则结果为模块名.


# print("__name__:", __name__)
if __name__ == "__main__":
    print("hello")
