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
    if type(t) == list:
        t = list(map(lambda x: str(x), t))
        out_string = "{" + " ".join(t)[:-1] + "}"
        print(out_string)
        return out_string
    elif type(t) == dict:
        out_string = o(t)
        print(out_string)
        return out_string
    else:
        obj_dict = vars(t)
        del obj_dict['_has']
        out_string = (o(vars(t)))
        print(out_string)
        return out_string

def o(t):
    out_string = "{"
    for k,v in t.items():
        out_string += ":" + str(k) + " " + str(v) + " "
    out_string = out_string.strip()
    out_string += "}"
    return out_string


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

def parse_csv(fname, fun=None, sep=','):
    with open(fname, "r") as src:
        lines_csv = src.readlines()
        for line in lines_csv:
            row = line.split(sep)
            if fun:
                fun(row)
        

def create_the():
    the = {}
    tup_list = re.findall(r'[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)', help)

    for k,x in tup_list:
        the[k] = coerce(x)
    return the

the = create_the()
            
def copy(t):
    if type(t) != dict:
        return t
    u = {}
    for k, v in t.items():
        u[k] = copy(v)
    return u
