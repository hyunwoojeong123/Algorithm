N,K = map(int,input().split())
def bottles(N):
    cnt = 0
    for i in range(24):
        if N & (1 << i):
            cnt += 1
    return cnt

buy = 0

while True:
    bts = bottles(N+(1<<buy))
    if bts <= K:
        break
    buy += 1
else:
    buy = -1
print(1<<buy)
