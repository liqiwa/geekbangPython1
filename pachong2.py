from urllib import parse
from urllib import request
# import socket
# # data = bytes(parse.urlencode({'word':'hello'}),encoding='utf-8')
# #
# # response = request.urlopen('http://httpbin.org/post',data=data)
# # print(response.read().decode('utf-8'))
#
# socket.timeout
import socket
import urllib
try:
    response3 = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:#错误类型不为urllib.error.URLError 异常不能捕获，Time Out 不能打印。
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
except socket.timeout: #添加 对应的异常类型 进行打印
    print('Time Out')