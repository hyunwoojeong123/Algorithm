

T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    linked = [[False for j in range(N+1)] for i in range(N+1)]
    visited = [False for i in range(N+1)]
    for _ in range(M):
        v1,v2 = list(map(int,input().split()))
        linked[v1][v2] = True
        linked[v2][v1] = True
    muri_cnt = 0
    for i in range(1,N+1):
        if not visited[i]:
            muri_cnt += 1
            visited[i] = True
            q = [i]
            while q:
                pi = q.pop(0)
                #print(pi)
                for ni in range(1,N+1):
                    if linked[pi][ni] and not visited[ni]:
                        q.append(ni)
                        visited[ni] = True
    print('#{} {}'.format(tc,muri_cnt))

