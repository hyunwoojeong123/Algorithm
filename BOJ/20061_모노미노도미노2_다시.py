def drop(t,x,y):
    # block을 해당 위치에 놓는다.
    pass

def all_pang():
    # 팡해서 점수 + 할게 있으면 한다.
    pass

def pale_clear():
    # 연한곳에 머가 있으면 밑에 칸 깎는다.
    pass

def green_full_check(i):
    # 그린의 해당 가로가 꽉 찼는지 체크
    for j in range(4):
        if not green[i][j]:
            return False
    return True

def blue_full_check(j):
    # 블루의 해당 세로가 꽉 찼는지 체크
    for i in range(4):
        if not blue[i][j]:
            return False
    return True

def green_remove(i):
    # 그린의 해당 가로를 없애고 위에 있는애가 밑으로 1칸 씩 밀리게 한다.
    for ii in range(0,i+1)[::-1]:
        for j in range(4):
            if ii == 0:
                green[ii][j] = False
            else:
                green[ii][j] = green[ii-1][j]

def blue_remove(j):
    # 블루의 해당 세로를 없애고 위에 있는애가 밑으로 1칸 씩 밀리게 한다.
    for jj in range(0,j+1)[::-1]:
        for i in range(4):
            if jj == 0:
                blue[i][jj] = False
            else:
                blue[i][jj] = blue[i][jj-1]


green = [[False for j in range(4)] for i in range(6)]
blue = [[False for j in range(6)] for i in range(4)]
N = int(input())
for _ in range(N):
    t,x,y = map(int,input().split())
    drop(t,x,y)
    all_pang()
    pale_clear()

