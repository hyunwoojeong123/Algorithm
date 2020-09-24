def hab(node):
    #print(node)
    if node >= N+1:
        return 0
    if tree[node] != 0:
        return tree[node]
    L,R = node*2,node*2+1
    return hab(L) + hab(R)

T = int(input())
for tc in range(1,T+1):
    N,M,L = list(map(int,input().split()))
    tree = [0 for _ in range(N+1)]
    for _ in range(M):
        n,val = list(map(int,input().split()))
        tree[n] = val
    print('#{} {}'.format(tc,hab(L)))