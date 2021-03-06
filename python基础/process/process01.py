"""
生活中，你可能一边听歌，一边写作业；一边上网，一边吃饭...这些都是生活的场景。电脑也可以执行多任务，比如可以同时打开浏览器等等...
简单的说就是多任务就是同一时间内运行多个程序


单核CPU实现多任务原理：操作系统轮流让各个任务交替执行，QQ执行2us,切换到微信，在执行2us，再切换到抖音...
每个任务反复执行下去，但是CPU调度执行速度太快了，导致我们感觉就像所有任务都在同一时间进行

多核CPU实现多任务原理：真正的并行执行多任务只能在多核CPU上实现，但是由于任务数量远远多于CPU的核心数量，所以，操作系统也会自动把很多
任务轮流调度到每个核心上执行

并发和并行
并发：当有多个线程在操作时，如果系统只有一个CPU，则它根本不可能真正同时进行一个以上的线程，它只能把CPU运行时间划分成若干个时间时间段，再将时间
段分配给各个线程执行，在一个时间段的线程代码运行时，其它线程处于挂起状态,这种称为并发

并行：当系统有一个以上CPU时，则线程的操作有可能并发。当一个CPU执行一个线程时，另一个CPU可以执行另一个线程，两个线程互不抢占CPU资源，可以同时进行，
这种方式称为并行

实现多任务的方式：
1.多进程模式
2.多线程模式
3.协程

进程 > 线程 > 协程

进程
优点：稳定性高，一个进程崩溃了不会影响其他进程、
缺点：①创建进程开销巨大  ②操作系统能同时运行的进程数目是有限的

from multiprocessing import Process

Process(target = 函数，name = 进程的名字，args = (给函数传递的参数))

对象调用方法：
Process.start()  启动进程并执行任务
Process.run()   知识执行了任务但是没有启动进程
terminate()  终止
"""
# 进程创建
import os
from multiprocessing import Process
from time import sleep

count = 0


def task1():
    global count
    while True:
        sleep(1)
        count += 1
        print("这是任务1....", os.getpid(), "-----", os.getppid(),count)


def task2():
    global count
    while True:
        sleep(2)
        count += 1
        print("这是任务2....", os.getpid(), "-----", os.getppid(),count)


'''
先执行主进程再执行子进程
'''
if __name__ == '__main__':
    print(os.getpid())
    # 子进程
    p1 = Process(target=task1, name="任务1")
    p1.start()
    print(p1.name)
    p2 = Process(target=task2, name="任务2")
    p2.start()
    print(p2.name)
    number = 0
    while True:
        number += 1
        sleep(0.2)
        if number == 100:
            p1.terminate()
            p2.terminate()
            break
        else:
            print(number)
    print("-" * 50)
