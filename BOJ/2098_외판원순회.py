ans = 987654321

def TSP(visit, now):
    visit |= (1 << now)
    if visit == (1 << N) - 1:
        if arr[now][0] > 0:
            return arr[now][0]
        return ans
    if d[visit][now] > 0:
        return d[visit][now]
    d[visit][now] = ans
    for i in range(N):
        if i != now and (visit & (1<<i)) == 0 and arr[now][i] > 0:
            temp = TSP(visit,i) + arr[now][i]
            if d[visit][now] > temp:
                d[visit][now] = temp
    return d[visit][now]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
d = [[0 for j in range(N)] for i in range(1 << N)]

ans = TSP(0,0)
if ans == 987654321:
    print(-1)
else:
    print(ans)