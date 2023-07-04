import socket
import multiprocessing
s = None

def check_online(ip_address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((ip_address, port))
        print(f"{ip_address}:{port} online")
    except Exception as e:
        print(f"{ip_address}:{port} offline  {e}")
    finally:
        s.close()

def start():
    with open("ip-source.txt") as file:
        dump = file.read()
        dump = dump.splitlines()


    pool = multiprocessing.Pool(processes=4)

    # Map the check_online function to each IP address in the dump list
    pool.starmap(check_online, [(ip, 443) for ip in dump])

if __name__ == "__main__" :
    start()