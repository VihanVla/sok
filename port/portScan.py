from Input import allinputs
import socket
Portlist = []
s = None

def checkPort(ip_address, port):

    n = None 
    while n != '-1':
        n = input("Give me your port number: ")
        Portlist.append(int(n))    
        print(Portlist)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        for port in Portlist:
                print(f"trying for port {port}")
                s.connect((ip_address, port))
                print(f"{ip_address} : {port} online")
    except Exception as e:
        print(f"{ip_address} : {port} offline")
    finally:
        s.close()