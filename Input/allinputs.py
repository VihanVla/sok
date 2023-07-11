IPlist=[]
class ipgetter:    
    def ipInput():
        n = None
        while n != '127.0.0.1':
            n = input("Give me your IP address: ")
            IPlist.append(n)    
            print(IPlist)
