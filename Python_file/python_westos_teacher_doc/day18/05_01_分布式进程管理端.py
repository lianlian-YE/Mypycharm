#!/usr/bin/env python
# coding:utf-8


""""
Name: 05_01_分布式进程管理端.py
Date: 2018/06/18
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import random
from queue import Queue
from multiprocessing.managers import BaseManager

# 1. 创建任务队列和任务执行结果的队列
task_queue = Queue()
result_queue = Queue()


# 2. 将队列通过网络暴露出去，让其他主机可以访问到队列;
class QueueManager(BaseManager):
    pass


# 3. 将两个队列都注册到网络上,
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)


#4. 绑定一个端口5001, 设置一个与其他主机共同直到的暗号/验证码;
#       0～65535
manager = QueueManager(address=('', 9999), authkey=b'westos')

# 5. 启动网络访队列的对象
manager.start()

# 6. 获取通过网络访问的对象
task = manager.get_task_queue()
result = manager.get_result_queue()



# 7. 放几个任务进去;
for i in range(100):
    n = random.randint(1, 1000)
    print('任务列表加入任务: %s' %(n))
    task.put(n)


# 8. 从result队列读取任务结果;
for j in range(100):
    r = result.get()
    print("队列任务的结果: %s" %(r))


# 8. 关闭
manager.shutdown()




