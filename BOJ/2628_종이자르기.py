M,N = map(int,input().split())
k = int(input())
ans = 0
garo,sero = [0],[0]
for _ in range(k):
    gs, p = map(int,input().split())
    if gs == 0:
        sero.append(p)
    else:
        garo.append(p)
sero.sort()
garo.sort()
garo.append(M)
sero.append(N)
for i in range(len(sero) -1):
    sr = sero[i+1] - sero[i]
    for j in range(len(garo) - 1):
        gr = garo[j+1] - garo[j]
        area = sr*gr
        if area > MAX:
            ans = area

print(ans)