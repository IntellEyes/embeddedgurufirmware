import sys
import os
su = "sudo"
es = "esptool.py"
po = "--port"
ser_port = sys.argv[1]
ba = "--baud"
ra = "460800"
wf = "write_flash"
fz = "--flash_size=8m 0"
fm = sys.argv[2]
a = '{} {} {} {} {} {} {} {} {}'.format(su, es, po, ser_port, ba, ra, wf, fz, fm)
#print(a)
os.system(a)

