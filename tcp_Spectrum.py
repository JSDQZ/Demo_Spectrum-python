
from socket import *

def open(ip,port):
    tcp_client_socket = socket(AF_INET,SOCK_STREAM)
    tcp_client_socket.settimeout(20)
    try:
        tcp_client_socket.connect((ip,port))
    except:
        print("Socket Connect ERROR")
        return -1
    return tcp_client_socket


def send(instr,cmd):
    try:
        cmd=cmd+'\r\n'
        instr.send(cmd.encode('utf-8'))
    except:
        print("Send Command ERROR")

def query(instr,cmd):
    try:
        cmd=cmd+'\r\n'
        instr.send(cmd.encode('utf-8'))
        recv_data=instr.recv(1024000)
    except:
        print("Query ERROR")
        return ''
    if recv_data:
        return recv_data.decode('utf-8')
    else:
        return ''

def close(instr):
    instr.close()




    
