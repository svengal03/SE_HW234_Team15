import pytest
from code import Num
from code import Sym
from code import Utils
import re
import sys
import random
from test import test_sample

def test_the():
    Utils.oo(the)
    return True

def test_sym():
    sym = Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000 * entropy) // 1 / 1000
    Utils.oo({"mid": mode, "div": entropy})
    return mode == "a" and 1.37 <= entropy and entropy <= 1.38


def test_num():
    num = Num()
    for i in range(1, 100):
        num.add(i)
    mid, div = num.mid(), num.div()
    print(mid, div)
    return 50 <= mid and mid <= 52 and 30.5 < div and div < 32


def test_bignum():
    num = Num()
    the['nums'] = 32
    for i in range(1, 1000):
        num.add(i)
    oo(num.nums())
    return 32 == len(num._has)


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
    for u, v in the.items():
        old[u] = v

    if the['dump'] == True:
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
        the[u] = v
