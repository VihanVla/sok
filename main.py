from checkOnline import checkOnline
from Input import allinputs

allinputs.ipInput()
allinputs.PortInput()


for ip_address in allinputs.IPlist :
    checkOnline.check_online(ip_address, port)