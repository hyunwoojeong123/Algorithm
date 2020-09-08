di = [0,0,1,-1]
dj = [1,-1,0,0]

def DFS(i,j,num):
    if len(num) == 7:
        nums.add(num)
        return
    for k in range(4):
        ni,nj = i + di[k], j + dj[k]
        if ni < 0 or nj < 0 or ni >= 4 or nj >= 4:
            continue
        DFS(ni,nj,num+board[i][j])

T = int(input())
for tc in range(1,T+1):
    board = [input().split() for i in range(4)]
    nums = set()
    for i in range(4):
        for j in range(4):
            DFS(i,j,'')
    print('#{} {}'.format(tc,len(nums)))