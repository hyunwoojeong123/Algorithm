for tc in range(1,11):
    V,E = list(map(int,input().split()))
    Edges = list(map(int,input().split()))
    linked = [[False for j in range(V+1)] for i in range(V+1)]
    for i in range(0,len(Edges),2):
        v1,v2 = Edges[i], Edges[i+1]
        linked[v1][v2] = True
    idx = [-1 for j in range(V+1)]
    for i in range(1,V+1):
        dist = [-1 for j in range(V+1)]
        q = [i]
        dist[i] = 0
        while q:
            pi = q.pop(0)
            for ni in range(1,V+1):
                if (dist[ni] == -1 or dist[ni] < dist[pi]+1) and linked[pi][ni]:
                    q.append(ni)
                    dist[ni] = dist[pi]+1
        #print(i,dist)
        for j in range(1,V+1):
            if idx[j] < dist[j]:
                idx[j] = dist[j]
    #print(idx)
    ans = ''
    for i in range(0,max(idx)+1):
        for j in range(1,V+1):
            if idx[j] == i:
                ans += str(j)
                ans += ' '
    print('#{} {}'.format(tc,ans))


