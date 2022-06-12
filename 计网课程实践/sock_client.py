import socket

# 定义服务器ip、端口
ip_ad=('127.0.0.1',9012)

# 创建socket对象
sk=socket.socket()

# 绑定ip端口
sk.bind(ip_ad)

# 开启监听
sk.listen()
print('服务器已经开启......')

# 等待接收客户端信息
conn,addr=sk.accept()
print('客户端地址:',addr)

# 等待接收客户端信息，接收到信息并非是字节格式，所以需要解码才能被正常识别【decode('utf-8')】
cli_data=conn.recv(1024).decode('utf-8')
print('接收到的客户端数据：',cli_data)

# 发送信息给客户端，发送的信息非字节格式，需要先转换格式【encode('utf-8'))】
sen_data=input('输入要发送的内容：')
conn.sendall(sen_data.encode('utf-8'))

# 断开连接
sk.close()
