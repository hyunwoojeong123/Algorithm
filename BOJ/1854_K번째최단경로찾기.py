import sys,heapq

def sort_insert(a,v):
    a_length = len(a)
    for i in range(a_length):
        if a[i] >= v:
            a.insert(i,v)
            break
    else:
        if a_length < k:
            a.append(v)
    if len(a) > k:
        a.pop()


n,m,k = map(int,sys.stdin.readline().strip().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().strip().split())
    edges[a-1].append([c,b-1])

D = [[] for _ in range(n)]

D[0].append(0)
pq = [[0,0]]
while pq:
    cur_d,cur_node = heapq.heappop(pq)
    if len(D[cur_node]) >= k and cur_d > D[cur_node][-1]:
        continue
    for next_d,next_node in edges[cur_node]:
        next_d += cur_d
        if len(D[next_node]) < k or D[next_node][-1] > next_d:
            heapq.heappush(pq,[next_d,next_node])
            sort_insert(D[next_node],next_d)
# print(D)

for i in range(n):
    if len(D[i]) < k:
        print(-1)
    else:
        print(D[i][k-1])



