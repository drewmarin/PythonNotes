from pwn import *
import requests
import sys

def funtion3(s):
   print("\t{}".format(s))

funtion3("parameter")

add_4 = lambda x : x + 4
print(add_4(5))

print(sys.version)
print(sys.executable)
print(sys.platform)

x = requests.get('http://httpbin.org/get')
print(x.content)

print(cyclic(50))
print(cyclic_find("laaa"))

print(p32(0x13371337))
print(hex(u32(p32(0x13371337))))