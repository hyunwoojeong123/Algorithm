linked = []
V = -1
visited = []
flag = 0

def find_way(start,end):

    visited[start] = True
    #print(start)
    if start == end:
        global flag
        flag = 1
        return
    else:
        for v in range(1,V+1):
            if linked[start][v] and not visited[v]:
                find_way(v,end)



T = int(input())
for tc in range(1,T+1):
    V,E= list(map(int,input().split()))
    linked = [[False for j in range(V+1)] for i in range(V+1)]
    visited = [False for i in range(V+1)]
    flag = 0
    for _ in range(E):
        i1,i2 = list(map(int,input().split()))
        linked[i1][i2] = True
    start,end = list(map(int,input().split()))
    find_way(start,end)
    print('#{} {}'.format(tc, flag))
