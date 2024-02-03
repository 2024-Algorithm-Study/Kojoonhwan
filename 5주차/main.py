import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

A = defaultdict(list)
vis = [False] * 100000

def dfs(node):
    vis[node] = True
    if not A[node]:
        return 1, 0

    on, off = 1, 0
    for v in [v for v in A[node] if not vis[v]]:
        leaf_on, leaf_off = dfs(v)
        on += min(leaf_on, leaf_off)
        off += leaf_on
    return leaf_on, leaf_off

def solution(n, lighthouse):
    for node, v in lighthouse:
        A[node].append(v) 
        A[v].append(node) 

    on, off = dfs(1) 
    return min(on, off)