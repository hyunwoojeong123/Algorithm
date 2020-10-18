# Prim
# 1. 임의의 시작점 하나를 선택한다.
# 2. 이 시작점과 연결된 정점들의 거리를 업데이트 한다.
# 3. 선택된 정점들과 연결되어 있는 간선들 중에서, 가장 짧은 길이의 간선을 선택해서 연결해준다.
# 4. 가장 짧은 간선으로 연결되어 있는 정점을 선택하고, 정점들의 거리를 업데이트 한다.
# 5. 3 ~ 4 번의 과정을 N-1 번 만큼 반복해준다.

# 1) pq 이용한 prim
import heapq
V,E = map(int,input().split())
linked = [[] for _ in range(V+1)]
for _ in range(E):
    start,end,weight = map(int,input().split())
    linked[start].append([weight,end])
    linked[end].append([weight,start])

Select = [False for _ in range(V+1)]
pq = []
ans = 0
cnt = 1
for link in linked[1]:
    Distance,Next = link
    heapq.heappush(pq,[Distance,Next])
Select[1] = True
while pq:
    Distance,Cur = heapq.heappop(pq)
    if not Select[Cur]:
        Select[Cur] = True
        ans += Distance
        cnt += 1
        for link in linked[Cur]:
            nDistance,Next = link
            if not Select[Next]:
                heapq.heappush(pq,[nDistance,Next])
    if cnt == V:
        break

print(ans)

# 2) 배열 이용한 prim
V,E = map(int,input().split())
linked = [[] for _ in range(V+1)]
Select = [False for _ in range(V+1)]
dist = [987654321 for _ in range(V+1)]
for _ in range(E):
    start,end,weight = map(int,input().split())
    linked[start].append([end,weight])
ans = 0
dist[1] = 0
Select[1] = True
for link in linked[1]:
    Next,Distance = link
    dist[Next] = Distance

for i in range(1,V):
    Min_Cost = 987654321
    Min_Idx = -1
    for j in range(1,V+1):    
        if Select[j]:
            continue
        if Min_Cost > dist[j]:
            Min_Cost = dist[j]
            Min_Idx = j
    Select[Min_Idx] = True
    ans += Min_Cost

    for link in linked[Min_Idx]:
        Next,Distance = link
        if Select[Next]:
            continue
        if dist[Next] > Distance:
            dist[Next] = Distance
print(ans)


# Union-FInd
class DisjointSet:
    def __init__(self,n):
        self.data = [-1 for _ in range(n)]
        self.size = n
        
    def upward(self, change_list, index):
        value = self.data[index]
        if value < 0:
            return index
        
        change_list.append(index)
        return self.upward(change_list, value)
    
    def find(self, index):
        change_list = []
        result = self.upward(change_list, index)
        
        for i in change_list:
            self.data[i] = result
            
        return result
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.data[x] < self.data[y]:
            self.data[y] = x
        elif self.data[x] > self.data[y]:
            self.data[x] = y
        else:
            self.data[x] -= 1
            self.data[y] = x
            
        self.size -= 1

# Kruskal
V,E = map(int,input().split())
#linked = [[1000001 for j in range(V+1)] for i in range(V+1)]
edges = []
for _ in range(E):
    edges.append(list(map(int,input().split())))
# print(edges)
edges= sorted(edges,key =lambda x:x[2])
# print(edges)
set_id = DisjointSet(V+1)
ans = 0
for edge in edges:
    start,end,weight = edge
    if set_id.find(start) == set_id.find(end):
        continue
    else:
        ans += weight
        set_id.union(start,end)
    if set_id.size == 2:
        break
print(ans)        