import numpy as np
import keras as k
import pandas as pd
import matplotlib as plt
y = np.random.randn(10,10)
import sys
import os
dd
os.chdir("C:/Users/andre/github/SIMPs/Basic Code")

x = np.random.randn(20,20)


#basic formatting
mpo = " This is how you can make a list: \n\tPython  \n\tJava "
print(mpo)

mpo.title()
mpo.upper()
mpo.lower()
mpo.lstrip()
mpo.rstrip()
mpo.strip()

name = "bob"
name_2 = "james"

messgae = f"hello {name}, I am {name_2}"
messgae

g = 3.2**3.2

type(g)


0.1 + 0.2

12_000_000_000 * 1

12000000000*12




relnum = 1

x, y, z = relnum*2,relnum*3,relnum*4

z
y
x



np.abs(-1)



REL_VALUE = 12_000_000_000


re = REL_VALUE
re - 2
2 - REL_VALUE



PORT =  9090

import this



this_list = ["red","blue","yellow","purple","green","black","white"]
int_list = ['7', '6', '5', '4', '3', '2', '1']

for x in this_list:
    for y in this_list:
        if x == y:
            print()
        else:
            print(int(y)*int(x))



this_list[::-1] #revrese
this_list[:-1]
this_list[-1]
this_list[1]
this_list[1:3]




for x,y in range(0,len(this_list)):
    print(this_list[x].title() + " " + int_list[y])
