from checkOnline import checkOnline
from Input import allinputs

allinputs.ipInput()

for ip_address in allinputs.IPlist :
    checkOnline.check_online(ip_address, 443)