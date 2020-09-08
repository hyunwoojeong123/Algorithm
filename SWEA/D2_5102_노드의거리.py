T = int(input())
for tc in range(1,T+1):
    V,E = list(map(int,input().split()))
    linked = [[False for j in range(V+1)] for i in range(V+1)]
    #print('연결:')
    for e in range(E):
        s,g = list(map(int,input().split()))
        #print(s,g)
        linked[s][g] = True
        linked[g][s] = True
    #print('연결 끝')
    S,G = list(map(int,input().split()))
    dist = [-1 for v in range(V+1)]
    dist[S] = 0
    q = []
    q.append(S)
    ans = 0
    while q:
        pv = q.pop(0)
        #print(pv,dist[pv])
        if pv == G:
            ans = dist[G]
            break
        for nv in range(1,V+1):
            #print('linked[{}][{}]'.format(pv,nv),linked[nv][pv])
            if not linked[nv][pv]:
                continue
            #print('dist[{}] < dist[{}]'.format(nv,pv),dist[nv],dist[pv])
            if dist[nv] != -1:
                continue
            q.append(nv)
            dist[nv] = dist[pv]+1
    print('#{} {}'.format(tc,ans))


