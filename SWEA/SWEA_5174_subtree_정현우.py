def BFS(N):
    q = [N]
    cnt = 0
    while q:
        p = q.pop(0)
        cnt += 1
        for n in range(1,E+2):
            if linked[p][n]:
                q.append(n)
    return cnt

T = int(input())
for tc in range(1,T+1):
    E,N = list(map(int,input().split()))
    linked = [[False for j in range(E+2)] for i in range(E+2)]
    element = list(map(int,input().split()))
    for i in range(0,len(element),2):
        st,ed = element[i],element[i+1]
        #print(st,ed)
        linked[st][ed] = True
    print('#{} {}'.format(tc,BFS(N)))