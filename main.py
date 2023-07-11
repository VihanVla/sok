from checkOnline import checkOnline
from Input import allinputs


allinputs.ipgetter.ipInput()
for ip in allinputs.IPlist:
    checkOnline.onlineChecker.check_online(ip,443)
