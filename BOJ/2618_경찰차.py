import sys
sys.setrecursionlimit(2500)

# c1 c2 경찰1,2가 젤 최근 해결한 사건
def DFS(c1,c2):
    now = max(c1, c2)
    if now == W:
        return 0
    if D[c1][c2] != -1:
        return D[c1][c2]
    nxt = now+1
    #d1,d2 경찰1,2가 담 사건까지 가는데 걸리는 거리
    d1= abs(cases[c1][0] - cases[nxt][0]) + abs(cases[c1][1] - cases[nxt][1])
    d2= abs(cases[c2][0] - cases[nxt][0]) + abs(cases[c2][1] - cases[nxt][1])
    if c2 == 0:
        d2 = abs(N - cases[nxt][0]) + abs(N - cases[nxt][1])
    # pd1 : 경찰1을 보냈을떄 거리 , pd2 : 2를 보냈을 때 거리
    pd2 = DFS(c1,nxt)+d2
    pd1 = DFS(nxt,c2)+d1
    D[c1][c2] = min(pd1,pd2)

    return D[c1][c2]

def who(c1,c2):
    now = max(c1,c2)
    if now == W:
        return
    nxt = now + 1
    # d1,d2 경찰1,2가 담 사건까지 가는데 걸리는 거리
    d1 = abs(cases[c1][0] - cases[nxt][0]) + abs(cases[c1][1] - cases[nxt][1])
    d2 = abs(cases[c2][0] - cases[nxt][0]) + abs(cases[c2][1] - cases[nxt][1])
    if c2 == 0:
        d2 = abs(N - cases[nxt][0]) + abs(N - cases[nxt][1])
    # pd1 : 경찰1을 보냈을떄 거리 , pd2 : 2를 보냈을 때 거리
    pd2 = DFS(c1, nxt) + d2
    pd1 = DFS(nxt, c2) + d1
    if pd1 < pd2:
        print(1)
        who(nxt,c2)
    else:
        print(2)
        who(c1,nxt)


N = int(input())
W = int(input())
D = [[-1 for _ in range(W+1)] for _ in range(W+1)]

cases = [[1,1]]
for _ in range(W):
    i,j = map(int,input().split())
    cases.append([i,j])

# D에 최근에 해결한 사건번호를 기준으로 저장하자
print(DFS(0,0))

# 이미 구해놓은 D를 이용해서 찾는겨
who(0,0)