import pytest
from code import Num
#from Num import Num
from code import Sym
from code import Utils
from code import Data
import re
import sys
import random
from test import test_sample


def test_the():
    Utils.oo(Utils.the)
    return True

def test_sym():
    sym = Sym.Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000 * entropy) // 1 / 1000
    Utils.oo({"mid": mode, "div": entropy})
    return mode == "a" and 1.37 <= entropy and entropy <= 1.38


def test_num():
    num = Num.Num()
    for i in range(1, 100):
        num.add(i)
    mid, div = num.mid(), num.div()
    print(mid, div)
    return 50 <= mid and mid <= 52 and 30.5 < div and div < 32


def test_bignum():
    num = Num.Num()
    Utils.the['nums'] = 32
    for i in range(1, 1000):
        num.add(i)
    Utils.oo(num.nums())
    return 32 == len(num._has)


def test_data():
    d = ("../data/auto93.csv")
    for _,y in d.cols.y:
        Utils.oo(y)
    return True

def test_stats():
    data = Data.Data("../data/auto93.csv")
    print('xmid=', data.stats(2, data.cols.x, "mid"))
    print('xdiv=', data.stats(3, data.cols.x, "div"))
    print('ymid=', data.stats(2, data.cols.y, "mid"))
    print('ymid=', data.stats(3, data.cols.y, "div"))
    return True

def test_csv():
    global n 
    n=0
    
    def function_row(r):
        global n 
        n+=1
        return n if n>10 else Utils.oo(r)
    Utils.csv("../data/auto93.csv", function_row)
    return True

def ALL():
    tests = dir(test_sample)
    tests = list(filter(lambda x: x[0:4] == "test", tests))
    tests.remove("test_sample")

    status = True
    for t in tests:
        print("\n−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        kstatus = run_tests(t)
        if kstatus == False:
            status = False
    return status


def run_tests(k):
    tests = dir(test_sample)
    tests = list(filter(lambda x: x[0:4] == "test", tests))
    tests.remove("test_sample")

    if k not in tests and k != "ALL":
        return

    random.seed(0)

    old = {}
    for u, v in Utils.the.items():
        old[u] = v

    if Utils.the['dump'] == True:
        fun = getattr(test_sample, k)
        status = fun()
        print("!!!!!!", Utils.msg(status), k, status)
    else:
        try:
            fun = getattr(test_sample, k)
            status = fun()
            print("!!!!!!", Utils.msg(status), k, status)
        except:
            status = False
            print("!!!!!!", Utils.msg(status), k, status)

    for u, v in old.items():
        Utils.the[u] = v
