import math
import re
import sys
import random

help = """
CSV :   summarized csv file
(c) 2022 Tim Menzies<timm@ieee.org> BSD-2 license
USAGE: lua seen.lua (OPTIONS]
OPTIONS:
    -e  --eg        start-up example                        = None
    -d  --dump      on test failure, exit with stack dump   = false
    -f  --file      file with txt data                      = ../data/data.txt
    -h  --help      show help                               = false
    -n  --nums      number of nums to keep                  = 512
    -s  --seed      random seed                             = 10019
    -S  --Seperator feild separator                         = ,
"""

def per(t,p):
    p = math.floor(((p or .5) * len(t)) + .5)
    return t[math.max(1, min(len(t), p))]

def oo(t):
    print(str(t))
    return t

def msg(status):
    return "PASS" if status else "FAIL"

def coerce(s):
    def fun(s1):
        if s1 == "true":
            return True
        if s1 == "false":
            return False
        return s1
    return int(s) if s.isnumeric() else None or fun(s)

def create_the():
    the = {}
    tup_list = re.findall(r'[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)', help)

    for k,x in tup_list:
        the[k] = coerce(x)
    return the

the = create_the()
