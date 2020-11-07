def union(a,b):
    p[find_set(a)] = p[find_set(b)]

def find_set(a):
    if p[a] != a:
        p[a] = find_set(p[a])
    return p[a]

n,m = map(int,input().split())
p = [x for x in range(n+1)]
for _ in range(m):
    oper,a,b = map(int,input().split())
    if oper == 0:
        # a가 포함되어 있는 집합과 b가 포함되어 있는 집합 합친다.
        union(a,b)
    else:
        # a,b 가 같은 집합에 포함되어 있는가?
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')
