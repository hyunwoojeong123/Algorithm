def DFS(p1,p2,idx):
    if idx == W:
        return 0
    

N = int(input())
W = int(input())
cases = []
for _ in range(W):
    i,j = map(int,input().split())
    cases.append([i,j])

D = dict()
