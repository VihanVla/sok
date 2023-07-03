import socket
s = None

def check_online (ip_adddress, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip_adddress, port))
        print(f"{ip_adddress}:{port} online")
        s.close()
    except Exception as e:
        print(f"{ip_adddress}:{port} offline  {e}")
    finally:
        s.close
        
with open ("ip-source.txt") as file:
    dump = file.read()
    dump = dump.splitlines()

for ip in dump:
    isOnline = check_online(ip, 443)

