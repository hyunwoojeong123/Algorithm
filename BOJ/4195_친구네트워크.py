import sys
input = sys.stdin.readline

def find_parents(x):
    if p[x] != x:
        p[x] = find_parents(p[x])
    return p[x]

def union(x,y):
    if find_parents(x) != find_parents(y):
        x = find_parents(x)
        y = find_parents(y)
        p[x] = y
        cnts[y] += cnts[x]

T = int(input())
for tc in range(1,T+1):
    F = int(input())
    p = dict()
    # cnts = dict()
    for _ in range(F):
        a,b = input().split()
        if a not in p:
            p[a] = a
            cnts[a] = 1
        if b not in p:
            p[b] = b
            cnts[b] = 1
        union(a,b)
        rt = find_parents(a)
        print(cnts[rt])