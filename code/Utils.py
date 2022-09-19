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

def per(t, p = 0.5):
    p = math.floor((p * len(t)) + 0.5)
    return t[max(1, min(len(t), p))]

def oo(t):
    print(str(t))
    return t

def msg(status):
    return "PASS" if status else "FAIL"


        
def coerce(s):
    s = s.strip()
    if s.isnumeric():
        return int(s)
    else:
        try:
            return float(s)
        except ValueError:
            if s == 'true' or s == 'TRUE' or s == 'True':
                return True
            elif s == 'false' or s == 'FALSE' or s == 'False':
                return False
            return re.match("\s*(.*)\s*", s).string

def parse_csv(src, func, separator):
    lines = src.split('\n')
    for line in lines:
        temp = []
        for ele in line.split(separator):
            ele = coerce(ele)
            temp.append(ele)
            #func(t)
        

def create_the():
    the = {}
    tup_list = re.findall(r'[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)', help)

    for k,x in tup_list:
        the[k] = coerce(x)
    return the

the = create_the()

def csv(fname, fun, sep=','):
    with open(fname, "r") as src:
        lines_csv = src.readlines()
        for line in lines_csv:
            row = line.split(sep)
            fun(row)
            
def copy(t):
    if type(t) != dict:
        return t
    u = {}
    for k, v in t.items():
        u[k] = copy(v)
    return u
