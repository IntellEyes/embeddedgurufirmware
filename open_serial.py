su = "sudo"
mi = "minicom"
pa = "-D"
import sys
import os
ser_port=sys.argv[1]
a = '{} {} {} {}'.format(su, mi, pa, ser_port)
os.system(a)
#print(ser_port)
#print(a)
