T = int(input())
for tc in range(1,T+1):
    N = int(input())
    N //= 10
    #print(N)
    d = [0 for i in range(N+1)]
    d[0],d[1],d[2] = 1,1,3
    for n in range(3,N+1):
        d[n] = d[n-1] + 2*d[n-2]
    print('#{} {}'.format(tc,d[N]))
