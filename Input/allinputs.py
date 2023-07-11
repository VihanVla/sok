IPlist = []
Portlist = []

def ipInput():
    n = None 
    while n != '127.0.0.1':
        n = input("Give me your IP address: ")
        IPlist.append(n)    
        print(IPlist)

def PortInput():
    n = None 
    while n != '-1':
        n = input("Give me your port number: ")
        Portlist.append(n)    
        print(Portlist)
