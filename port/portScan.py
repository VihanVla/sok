import socket
s = None

def checkPort(ip_address, port):
    print(f"trying for port {port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((ip_address, port))
        print(f"{ip_address}:{port} online")
    except Exception as e:
        print(f"{ip_address}:{port} offline  {e}")
    finally:
        s.close()