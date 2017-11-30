# -*- coding:utf-8- -*-
# Author：Ethandyp
# formult = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
#
#
# # formult.replace("40","B")
# # print formult
#
# print formult.replace(" ","")

import re

s = "2*15/3"

def cx(n_l,c_l):
    for i in range(0,len(c_l)):
        if c_l and c_l[i] == "*":
            n_l[i+1] = int(n_l[i]) * int(n_l[i+1])
            del n_l[i]
            del c_l[i]
            if c_l:
                cx(n_l,c_l)
            continue
        if c_l and c_l[i] == "/":
            n_l[i+1] = int(n_l[i]) / int(n_l[i+1])
            del n_l[i]
            del c_l[i]
            if c_l:
                cx(n_l,c_l)
            continue
    return n_l


m = re.split("[\*\/]",s)
n = re.findall("([\*\/])",s)
# print m
# print n
print cx(m,n)
