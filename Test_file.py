# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 09:21:48 2018

@author: shuyan
"""

#This library tests smrtlib.py
import smrtlib
for x in range(3001,3020):
    print(smrtlib.emu_to_vobc(x))
print(smrtlib.emu_to_vobc("a"))
print(smrtlib.emu_to_vobc("3001"))
print(smrtlib.emu_to_vobc("         3001   "))


for x in range(1001,1020):
    print(smrtlib.vobc_to_emu(x))
print(smrtlib.vobc_to_emu("a"))
print(smrtlib.vobc_to_emu("1001"))
print(smrtlib.vobc_to_emu("         1001   "))


for x in range(3001,3020):
    print(smrtlib.emu_to_emu2(x))
print(smrtlib.emu_to_emu2("a"))
print(smrtlib.emu_to_emu2("3001"))
print(smrtlib.emu_to_emu2("         3001   "))


for x in range(1001,1020):
    print(smrtlib.vobc_to_emu2(x))
print(smrtlib.vobc_to_emu2("a"))
print(smrtlib.vobc_to_emu2("1001"))
print(smrtlib.vobc_to_emu2("         1001   "))


for x in range(3001,3020):
    print(smrtlib.emu_to_type(x))
print(smrtlib.emu_to_type("a"))
print(smrtlib.emu_to_type("3001"))
print(smrtlib.emu_to_type("         3001   "))
print(smrtlib.emu_to_type("1404"))
print(smrtlib.emu_to_type("1435"))
print(smrtlib.emu_to_type("1451"))

for x in range(3001,3020):
    print(smrtlib.emu_to_name(x))
print(smrtlib.emu_to_name("a"))
print(smrtlib.emu_to_name("3001"))
print(smrtlib.emu_to_name("         3001   "))
print(smrtlib.emu_to_name("1404"))
print(smrtlib.emu_to_name("1435"))
print(smrtlib.emu_to_name("1451"))