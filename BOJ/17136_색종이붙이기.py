# 모든 1을 덮는데 필요한 색종이의 최소 개수
# 1을 모두 덮는 것이 불가능한 경우에 -1을 출력
# 1x1 ~ 5x5 각 5개씩
# 완전탐색
# 배열 첨부터 끝까지 차례대로 돈다.
# 1을 만나면 1x1 ~ 5x5 색종이를 붙일 수 있으면 붙인다.
# cnt 줄이거 넘어간다.
# 1이 적힌 칸은 모두 색종이, 0이 적힌 칸은 안대 겹쳐도 안대
def paper_chk(i,j,sz):
    for ii in range(i,i+sz):
        for jj in range(j,j+sz):
            if ii < 0 or ii >= 10 or jj < 0 or jj >= 10:
                return False
            if covered[ii][jj] or arr[ii][jj] == 0:
                return False
    return True

def attach_paper(i,j,sz):
    for ii in range(i,i+sz):
        for jj in range(j,j+sz):
            covered[ii][jj] = True


def detach_paper(i,j,sz):
    for ii in range(i,i+sz):
        for jj in range(j,j+sz):
            covered[ii][jj] = False

def is_all_covered():
    for i in range(10):
        for j in range(10):
            if arr[i][j] and not covered[i][j]:
                return False
    return True

def DFS(idx,cnts):
    global ans
    if sum(cnts) >= ans:
        return
    if idx == 100:
        if sum(cnts) < ans and is_all_covered():
            ans = sum(cnts)
        return
    i = idx // 10
    j = idx % 10
    #print('DFS', i,j)
    if arr[i][j] == 0 or covered[i][j]:
        DFS(idx+1,cnts)
    else:
        for sz in range(1,6):
            #print(sz)
            if cnts[sz] >= 5:
                continue
            if paper_chk(i,j,sz):
                attach_paper(i,j,sz)
                cnts[sz] += 1
                DFS(idx+1, cnts)
                cnts[sz] -= 1
                detach_paper(i,j,sz)
                #DFS(idx+1, cnts)


arr = [list(map(int,input().split())) for _ in range(10)]
covered = [[False for _ in range(10)] for _ in range(10)]
cnts = [0,0,0,0,0,0] # 쓴 색종이 개수
ans = 987654321
DFS(0,cnts)
if ans == 987654321:
    ans = -1
print(ans)
