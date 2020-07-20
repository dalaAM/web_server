
"""
类的使用方法
1.类中的所有方法都可以被类中的任意一个方法调用
2.类属性（参数）可以被类中任意一个方法
3.类属性（参数）只是一个类中使用的全局变量，类中所有的方法都可以调用

finally：无论怎样都要做

类中要传的参数主要是


类的设计原则
1.站在用户的角度，想问题
2.能替用户做决定的，不要麻烦用户
3.
编写程序
先分析，然后在写程序

 “”“
 思考问题：1.使用流程
         2.那些量需要用户决定的，那些量需要传递进来，怎么传参
                哪组网页， 服务端地址

"""

from socket import *
from select import select

class WebServer:
    def __init__(self,host = '0.0.0.0',port = 80,html = None):
        #传入参数
        self.host =host
        self.port =port
        self.html =html
        self.__rlist =[]
        self.__wlist =[]
        self.__xlist =[]
        self.create.sock()
        self.sock.bind()

    #创建tcp套接字
    def create(self,sock):
        self.sock = sock
        self.sock =socket()





    pass


    def start(self):
        pass

if __name__ == '__main__':


    webuser = WebServer(host  = '0.0.0.0',port =8888,html =None)
    webuser.start()
