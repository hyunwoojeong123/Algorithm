# blue는 4x6 , green은 6x4
from pprint import pprint

def cnt_pale(color):
    ret = 0
    if color == 'green':
        for i in range(0,2):
            for j in range(0,4):
                if green[i][j]:
                    ret += 1
                    break
    else:
        for j in range(0,2):
            for i in range(0,4):
                if blue[i][j]:
                    ret += 1
                    break
    return ret

def pale_clear(color):
    if color == 'green':
        gp = cnt_pale(color)
        # for i in range(0, 2):
        #     for j in range(0, 4):
        #         green[i][j] = False
        for i in range(6-gp,6)[::-1]:
            for j in range(4):
                #green[i][j] = False
                for ii in range(0,i+1)[::-1]:
                    if ii == 0:
                        green[ii][j] = False
                    else:
                        green[ii][j] = green[ii-1][j]
    else:
        bp = cnt_pale(color)
        # for j in range(0, 2):
        #     for i in range(0, 4):
        #         blue[i][j] = False

        for j in range(6-bp,6)[::-1]:
            # 해당 줄 다 지우기
            for i in range(4):
                #blue[i][j] = False
                for jj in range(0,j+1)[::-1]:
                    if jj == 0:
                        blue[i][jj] = False
                    else:
                        blue[i][jj] = blue[i][jj-1]
def pang():
    # green 보드의 가로
    # blue 보드의 세로가 가득 차 있으면, 다 없애고 그 위에 있는 애들은
    # 내려간다.
    global score
    for j in range(6):
        cnt = 0
        for i in range(4):
            if blue[i][j]:
                cnt += 1
        if cnt == 4:
            score += 1
            for i in range(4):
                blue[i][j] = False
                if j != 0:
                    for jj in range(0,j+1)[::-1]:
                        if jj == 0:
                            blue[i][jj] = False
                        else:
                            blue[i][jj] = blue[i][jj-1]

    for i in range(6):
        cnt = 0
        for j in range(4):
            if green[i][j]:
                cnt += 1
        if cnt == 4:
            score += 1
            # 다 없애고 그 위에 있는 애들 내린다
            for j in range(4):
                green[i][j] = False
                if i != 0:
                    for ii in range(0,i+1)[::-1]:
                        if ii == 0:
                            green[ii][j] = False
                        else:
                            green[ii][j] = green[ii-1][j]



def drop(t,i,j):
    #print('drop({},{},{})'.format(t,i,j))
    if t == 1:
        # t = 1. 블럭 1x1놓을떄
        # (i,j) 위치에 놓으면,
        # 파란색 보드는 i는 유지대고 j는 오른쪽에서 블록없는 젤 끝에
        for jj in range(0,6):
            if blue[i][jj]:
                blue[i][jj-1] = True
                break
        else:
            blue[i][5] = True
        # 초록색 보드는 j는 유지되고 i는 밑에서 블록없는 맨 끝에
        for ii in range(0,6):
            if green[ii][j]:
                green[ii-1][j] = True
                break
        else:
            green[5][j] = True

    elif t == 2:
        # t = 2. 블럭 1x2 놓을때
        # (i,j), (i,j+1) 위치에 놓으면,
        # 파란색 보드는 i는 유지대고 j+1은 오른쪽에서 블록없는 맨 끝에 j는 그 왼쪽
        for jj in range(0,6):
            if blue[i][jj]:
                blue[i][jj-1] = True
                blue[i][jj-2] = True
                break
        else:
            blue[i][5] = True
            blue[i][4] = True
        # 초록색 보드는 j,j+1은 유지대고 i는 j,j+1 중에 블록없는 맨 끝에
        for ii in range(0,6):
            if green[ii][j] or green[ii][j+1]:
                green[ii-1][j] = True
                green[ii-1][j+1] = True
                break
        else:
            green[5][j] = True
            green[5][j+1] = True
    else:
        # t = 3. 블럭 2x1 놓을때
        # (i,j) , (i+1, j) 위치에 놓으면,
        # 파란색 보드는 i,i+1은 유지대고 j는 오른쪽에서 블록없는 맨끝에
        for jj in range(0,6):
            if blue[i][jj] or blue[i+1][jj]:
                blue[i][jj-1] = True
                blue[i+1][jj-1] = True
                break
        else:
            blue[i][5] = True
            blue[i+1][5] = True
        # 초록색 보드는 j은 유지대고 i,i+1는 밑에서 블록없는 맨 끝에
        for ii in range(0,6):
            if green[ii][j]:
                green[ii-1][j] = True
                green[ii-2][j] = True
                break
        else:
            green[5][j] = True
            green[4][j] = True

N = int(input())
score = 0
blue = [[False for _ in range(6)] for _ in range(4)]
green = [[False for _ in range(4)] for _ in range(6)]
for _ in range(N):
    t,x,y = map(int,input().split())
    drop(t,x,y)
    # print('drop한 후')
    # pprint(blue)
    # pprint(green)
    pang()
    # print('pang한 후')
    # pprint(blue)
    # pprint(green)
    pale_clear('green')
    pale_clear('blue')
    # print('pale clear한 후')
    # pprint(blue)
    # pprint(green)

green_cnt = 0
blue_cnt = 0

for i in range(6):
    for j in range(4):
        if green[i][j]:
            green_cnt += 1

for i in range(4):
    for j in range(6):
        if blue[i][j]:
            blue_cnt += 1

print(score)
print(green_cnt+blue_cnt)