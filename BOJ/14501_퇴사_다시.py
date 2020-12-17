def DFS(day,cost):
    global ans
    # print(day,cost)
    if day >= N:
        if cost > ans:
            ans = cost
        # print('끝!')
        return

    if day+Ts[day] <= N:
        DFS(day+Ts[day],cost+Ps[day])
    DFS(day+1,cost)


N = int(input())
Ts, Ps = [], []
ans = -1
for _ in range(N):
    T,P = map(int,input().split())
    # print(T,P)
    Ts.append(T)
    Ps.append(P)
# print(Ts,Ps)
DFS(0,0)
print(ans)