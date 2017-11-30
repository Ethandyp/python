# -*- coding:utf-8- -*-
# Author：Ethandyp

import re

def matchlp(data):
    res = []
    for n in range(len(data)):
        if data[n] == "(":
            res.append(n)
            continue
        if data[n] == ")":
            #print data[res[-1]:n+1]
            a = data[res[-1]:n+1]
            data = data.replace(a,"A".center(len(a)))
            res.pop()
    print data
    return

def calcu(s):

    return


formult = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"

# m = re.findall("\(([^()]+)\)",formult)
# print m
#
# for i in formult:
#     print i,
#
# for i in range(len(formult)):
#     print formult[i],
#
# for n,s in enumerate(formult):
#     print "%d:%s " % (n,s),
matchlp(formult)