from checkOnline import checkOnline
from Input import ipInput

ipInput.ipInput()

for ip_address in ipInput.IPlist :
    checkOnline.check_online(ip_address, 443)