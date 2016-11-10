import sys
import os
su = "sudo"
es = "esptool.py"
po = "--port"
ef = "erase_flash"
ser_port = sys.argv[1]
a = '{} {} {} {} {}'.format(su, es, po, ser_port, ef)
os.system(a)
#print(a)
