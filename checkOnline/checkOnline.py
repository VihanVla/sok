import socket
import port.portScan as portScan
from Input import allinputs
s = None
class onlineChecker:
        
        def check_online(ip_address, port):
            print(f"trying for ip {ip_address}")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.connect((ip_address, port))
                print(f"{ip_address}:{port} online")
                portScan.checkPort(ip_address, port)
            except WindowsError:
                print("offline")
            except Exception as e:
                print(f"{ip_address}:{port} offline  {e}")
            finally:
                s.close()