def weight(root):
    visited[root] = True
    child_weights = []
    # 만약 자식 없으면 1 리턴
    for dist,next in adj[root]:
        if visited[next]:
            continue
        child_weights.append(dist*weight(next))
    # 있으면 배열 1개에 다 넣어놈
    if child_weights == []:
        return 1
    else:
        # 배열에 넣은애들 다 더해서 리턴
        ret = 0
        for i in range(len(child_weights)):
            for j in range(i+1,len(child_weights)):
                ret += child_weights[i][j]


N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    A,B,W = map(int,input().split())
    adj[A].append([W,B])
    adj[B].append([W,A])
visited = [False for _ in range(N+1)]
print(weight(1))