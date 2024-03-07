import sys

from functools import cache
from collections import defaultdict

sys.setrecursionlimit(2000)

@cache
def rec(num:int)->int:
    if num == 1:
        return 0

    return rec(num//2) + rec((num+1)//2) + num

if __name__ == '__main__':
    N = int(input())

    print(rec(N))