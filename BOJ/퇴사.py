ans = -1
def DFS(day,margin):
    #print(day,margin)
    global N,ans
    if day > N:
        if ans < margin:
            ans = margin
        return
    # 상담 안하고 넘어가는 경우
    DFS(day+1,margin)
    # 상담 하는 경우
    # 상담이 가능한 경우에만 함
    if day+time[day] <= N+1:
        DFS(day+time[day],margin+gain[day])



N = int(input())
time,gain = [-1],[-1]
for _ in range(N):
    t,g = list(map(int,input().split()))
    time.append(t)
    gain.append(g)

DFS(1,0)
print(ans)