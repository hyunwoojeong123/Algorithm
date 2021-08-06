def dokrib(now,last_in,pnode):
    # print(now,last_in,pnode)

    # 종료조건은 child가 없으면 알아서 리턴댐
    # if D[last_in] != -1:
    #     return D[last_in]
    # 방문 처리
    # now를 포함한 경우와 안포함한 경우를 구해서

    now_in, now_not_in = weight[now],0
    if last_in == pnode:
        now_in = 0
    # child들을 순회하며 합해준다.
    for child in edges[now]:
        if child == pnode:
            continue
        # now를 포함한 경우
        # 이 때는 last_in이 부모인지만 보면됨
        if last_in != pnode:
            now_in += dokrib(child,now,now)
        # now를 포함하지 않은 경우
        now_not_in += dokrib(child,last_in,now)
    # 둘중 더 큰애를 D에 저장하고 리턴
    if now_in > now_not_in:
        jibhab.add(now)
    D[last_in] = max(now_in,now_not_in)
    return D[last_in]

n = int(input())
visited = [False for _ in range(n+1)]
weight =[-1] + list(map(int,input().split()))
D = [-1 for j in range(n+1)]
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)
jibhab = set()
print(dokrib(1,0,-1))
real = []
for each in jibhab:
    real.append(each)
real.sort()
dokribs = ''
for i in range(len(real)):
    dokribs += str(real[i])
    if i != len(real)-1:
        dokribs += ' '
print(dokribs)