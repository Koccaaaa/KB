import socket

# 创建socket对象
sk=socket.socket()

# 连接服务器ip及商品
sk.connect(('127.0.0.1',9012))

# 向服务器发送信息，需要先转换格式【encode('utf-8'))】，才能被服务器识别
sen_data=input('输入要发送的内容：')
sk.sendall(sen_data.encode('utf-8'))

# 接收来自服务器的信息，接收到信息并非是字节，所以需要解码才能被正常识别
ser_data=sk.recv(1024).decode('utf-8')
print('接收到的服务端数据：',ser_data)

# 断开连接
sk.close()


