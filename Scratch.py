def funtion3(s):
   print("\t{}".format(s))

funtion3("parameter")

add_4 = lambda x : x + 4
print(add_4(5))

import sys

print(sys.version)
print(sys.executable)
print(sys.platform)


import requests
x = requests.get('http://httpbin.org/get')
print(x.content)

from pwn import *

print(cyclic(50))
print(cyclic_find("laaa"))

print(shellcraft.sh)