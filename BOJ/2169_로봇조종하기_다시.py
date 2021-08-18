import sys

N,M = map(int, sys.stdin.readline().rstrip().split())
arr = []
D = [[[-1 for k in range(3)] for j in range(M)] for i in range(N)]

for _ in range(N):
    tp = list(map(int,sys.stdin.readline().rstrip().split()))
    arr.append(tp)

# D 0 : 전체 저장 1: 왼쪽으로 진행할때 2: 오른쪽으로 진행할때
# 첫째줄은 오른쪽 진행으로 쭉 채운다
D[0][0][0] = arr[0][0]

for j in range(1,M):
    D[0][j][0] = D[0][j-1][0] + arr[0][j]

# print(D)
# 둘째줄부터는 1,2 배열을 먼저 채우는데 얘네는 진행방향과 위에서 오는거 비교해서 큰걸로 계속 채운다

for i in range(1,N-1):
    D[i][0][2] = D[i-1][0][0] + arr[i][0]
    for j in range(1,M):
        D[i][j][2] = max(D[i-1][j][0] + arr[i][j], D[i][j-1][2] + arr[i][j])

    D[i][M-1][1] = D[i-1][M-1][0] + arr[i][M-1]
    for j in range(M-1)[::-1]:
        D[i][j][1] = max(D[i-1][j][0] + arr[i][j], D[i][j+1][1] + arr[i][j])

    for j in range(M):
        D[i][j][0] = max(D[i][j][1],D[i][j][2])
# 그다음 0 배열을 채우는데 둘 중 큰 애로 채운다
# 마지막 줄은 오른쪽 진행만 가능하다

if N != 1:
    D[N-1][0][0] = D[N-2][0][0] + arr[N-1][0]
    for j in range(1,M):
        D[N-1][j][0] = max(D[N-2][j][0] + arr[N-1][j], D[N-1][j-1][0] + arr[N-1][j])

print(D[N-1][M-1][0])
# print(arr)
# print(D)
