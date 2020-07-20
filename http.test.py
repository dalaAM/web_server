"""
http test


思路：
1.创建socket，tcp套接字
2.建立多客户端网络并发模型
"""

from socket import *

s=socket()
s.bind(('0.0.0.0',8888))
s.listen(5)

connfd,addr = s.accept()
print("connect from:",addr)
data = connfd.recv(4096)
print(data.decode())


#响应格式
http ="""HTTP/1.1 200 OK
Connect-type:text/html

"""


connfd.send(http.encode())
