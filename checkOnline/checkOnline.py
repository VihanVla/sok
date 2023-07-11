import socket
s = None

def check_online(ip_address, port):
    print(f"trying fo {ip_address}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((ip_address, port))
        print(f"{ip_address}:{port} online")
    except WindowsError:
        print("offline")
    except Exception as e:
        print(f"{ip_address}:{port} offline  {e}")
    finally:
        s.close()