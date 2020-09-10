def maketree(i):
    global num
    if i > N:
        return
    left,right = i*2,i*2+1
    maketree(left)
    tree[i] = num
    num += 1
    maketree(right)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0 for x in range(N+1)]
    num = 1
    maketree(1)
    print('#{} {} {}'.format(tc,tree[1],tree[N//2]))