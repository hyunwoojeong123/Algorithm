import sys
sys.stdin = open('input.txt','r')

di = [0,0,1] #오,왼,아래
dj = [1,-1,0]
ans = -1
min_dist = 99999999
def check(i,j,dist):
    visited[i][j] = True
    print(i,j)
    #종료조건
    #i,j가 마지막 칸에 도달했을 때 찾기 성공
    if i == 99:
        return True
    #i가 마지막 행이지만 j가 마지막이 아닐때는 찾지 못한것
    # elif i == 99 and j != 99:
    #     return False

    #범위 체크도 해줄거야
    # D = len(di)
    else:
        for d in range(3):
            #다음 위치 지정
            ni = i + di[d]
            nj = j + dj[d]
            #idx가 벗어나지 않고, 그 값이 0이 아니면 방문하지 않았던 곳으로 갈거야
            if ni >= 0 and ni < 100 and nj >= 0 and nj < 100 and ladder[ni][nj] != 0 and visited[ni][nj] == False:

                # 양옆중 1이 있는지 확인, 있다면 그 곳으로 방향 전환
            # if ni < 0 or ni >= 100 or nj < 0 or nj >= 100:
            #     continue
            # if ladder[ni][nj] == 0:
            #     continue
            # if visited[ni][nj]:
            #     continue
                print(ni, nj, ladder[ni][nj], visited[ni][nj])
                return check(ni,nj,dist+1) #반복


for tc in range(1,11):
    T = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    visited = [[False for j in range(100)] for i in range(100)]
    start = [] #start지점들을 넣어줄거야
    for j in range(100):
        if ladder[0][j] == 1:
            start.append(j)
    #start지점들을 돌면서 체크할거야
    for s in start:
        #start마다 방문체크 리셋
        visited = [[False for i in range(100)] for j in range(100)]
        if check(0,s): #제일 첫 출발점부터 볼거야!
            print('#{} {}'.format(tc,s))
            break #값을 찾았으니 멈춰라