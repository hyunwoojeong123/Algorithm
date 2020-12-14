# X 시간 후 활성화 X 시간만큼 생존
# 죽으면 그 상태로 셀 차지
# 활성화 후 첫 1시간만 번식
# 4방향으로 번식, 번식 된애는 비활성
# 이미 줄기세포 있으면 글로 안감
# 두 개 이상의 줄기세포가 동시에 갈려하면 생명력 높은애가 차지
# 배양용기의 크기는 무제한
# 배양시간 K 후 총 줄기 세포의 개수 구해

di = [0,0,1,-1]
dj = [1,-1,0,0]
sz = 400
from pprint import pprint

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = [[[0,0,0] for j in range(sz)] for i in range(sz)]
    ips = [list(map(int,input().split())) for _ in range(N)]
    si,sj = sz//2 - N//2, sz//2 - M//2
    for i in range(N):
        for j in range(M):
            # print('arr[{}][{}] = ips[{}][{}]'.format(si+i,sj+j,i,j))
            if ips[i][j] != 0:
                arr[si+i][sj+j] = [ips[i][j],ips[i][j]+1,0+ips[i][j]*2]

    t = 0
    while t < K:

        t += 1
        for i in range(sz):
            for j in range(sz):
                if arr[i][j] != [0,0,0] and arr[i][j][1] == t:
                    for k in range(4):
                        ni,nj = i+di[k],j+dj[k]
                        if arr[ni][nj] == [0,0,0] or (arr[ni][nj] != [0,0,0] and arr[ni][nj][1]-1-arr[ni][nj][0] == t and arr[ni][nj][0] < arr[i][j][0]):
                            arr[ni][nj] = [arr[i][j][0], arr[i][j][0] + t + 1, t + arr[i][j][0]*2]

        # print(t)
        # for i in range(sz):
        #     for j in range(sz):
        #         print(arr[i][j], end = ' ')
        #     print()
    ans = 0
    for i in range(sz):
        for j in range(sz):
           if arr[i][j] != [0,0,0] and arr[i][j][2] > K:
               ans += 1
    print('#{} {}'.format(tc, ans))
