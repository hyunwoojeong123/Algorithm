di = [-1,-1,1,0,0] # 상 하 좌 우
dj = [-1,0,0,-1,1]
rev= [-1,2,1,4,3]
from pprint import pprint

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = [[[] for j in range(N)] for i in range(N)]
    planks = []
    for _ in range(K):
        i,j,num,dir = map(int,input().split())
        planks.append([i,j,num,dir])
    t = 0
    while t < M:
        t += 1
        tplanks = []
        for plank in planks:
            i,j,num,dir = plank
            ni,nj = i+ di[dir], j+dj[dir]
            # 약품자리면 미생물 반절로 줄이고 이동방향 바꾼다.
            if ni == 0 or nj == 0 or ni == N-1 or nj == N-1:
                num //= 2
                dir = rev[dir]
            tplanks.append([ni,nj,num,dir])
        planks = tplanks
        # print(t, '초')
        # print('planks:')
        # print(planks)
        # 그 다음에 뭉친애 합치기
        arr = [[[] for j in range(N)] for i in range(N)]
        for plank in planks:
            i,j,num,dir = plank
            arr[i][j].append([num,dir])

        # print('이동후')
        # pprint(arr)
        for i in range(N):
            for j in range(N):
                if len(arr[i][j]) >= 2:
                    arr[i][j] = sorted(arr[i][j],reverse=True)
                    dir = arr[i][j][0][1]
                    num = 0
                    for each in arr[i][j]:
                        num += each[0]
                    arr[i][j] = [[num,dir]]
        # print('합친후')
        # pprint(arr)
        planks = []
        for i in range(N):
            for j in range(N):
                if arr[i][j] != []:
                    planks.append([i,j,arr[i][j][0][0],arr[i][j][0][1]])
    ans = 0
    for plank in planks:
        ans += plank[2]
    print('#{} {}'.format(tc,ans))
