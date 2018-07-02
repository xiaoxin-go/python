"""
用Python实现一个HTTP web服务器，它知道如何运行服务器端CGI脚本：
从当前工作目录提供文件和脚本；Python脚本必须存储在 webdir\cgi-bin或
webdir\htbin中；
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'        # 存放HTML文件和cgi-bin脚本文件夹的所在
port = 80           # 缺省http://localhost/，也可以使用http://localhost:xxxx/

os.chdir(webdir)        #进入运行目录
srvaddr = ('',port)    #定义服务器地址和端口
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)     #创建HTTPServer对象
srvobj.serve_forever()      # 以守护进程永久运行