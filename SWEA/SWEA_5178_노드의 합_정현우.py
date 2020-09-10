T = int(input())
for tc in range(1,T+1):
    N,M,L = list(map(int,input().split()))
    tree = [0 for x in range(N+1)]
    for _ in range(M):
        node,val = list(map(int,input().split()))
        tree[node] = val
    for i in range(1,N-M+1)[::-1]:
        sum = 0
        left,right = i*2,i*2+1
        if left <= N:
            sum += tree[left]
        if right <= N:
            sum += tree[right]
        tree[i] = sum
    print('#{} {}'.format(tc,tree[L]))