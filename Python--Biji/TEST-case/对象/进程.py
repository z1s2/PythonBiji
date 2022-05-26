"""
进程是执行中的程序
拥有独立的地址空间、内存、数据栈（）---可以帮我使用多核cpu,一个进程适配一个一个cpu
操作系统管理
派生（fork或者spawn）新进程
进程间通信（ipc）方式共享信息
"""

"""
---什么是线程（python之间是多进程开始的）
同进程下执行，并共享相公的线上下文
线程间的信息共享和通信更加容易
多线程并发执行（交互的执行）----某一时刻执行一个线程
需要同步原语（不重要）
"""

"""
python与线程
python如何处理线程（解释性语言，代码实时运行）
解释器主循环
主循环中只有一个控制线程在执行
使用全局解释器锁（Gil）----同一时间只有一个线程，以此按照时间执行
GIL保证一个线程

"""
"""
设置GIL
切换进一个线程去运行
执行下面操作之一
    指定数量的字节码指令
    线程主动让出控制权
把线程设置回睡眠状态（切换出线程）
解锁GIL
"""


"""
_thread:提供了基本的线程和锁
threding的底层使用了_thread:提供了更高级别，功能更全面的线程管理
    支持同步机制
    支持守护进程
"""

import logging
from time import sleep,ctime

logging.basicConfig(level=logging.INFO)

def loop0():
    sleep(4)


#列表生成式
lis = [x*x for x in range(10)]
print(lis)
#生成器
generator_ex = (x*x for x in range(10))
for i in generator_ex:
    print(i)
#linux查看文件日志里含root的命令
#grep -n root test.txt
