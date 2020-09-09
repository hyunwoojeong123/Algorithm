def sunhwa(i):
    global ans
    #print(i)
    if len(adj[i]) == 2:
        left,right = adj[i][0],adj[i][1]
        sunhwa(left)
        ans += vals[i]
        sunhwa(right)
    elif len(adj[i]) == 1:
        left = adj[i][0]
        sunhwa(left)
        ans += vals[i]
    else:
        ans += vals[i]

for tc in range(1,11):
    N = int(input())
    adj = [[] for j in range(N+1)]
    vals = ['' for j in range(N+1)]
    ans = ''
    for _ in range(N):
        temp = input().split()
        ind = int(temp[0])
        val = temp[1]
        vals[ind] = val
        if len(temp) == 2:
            pass
        elif len(temp) == 3:
            adj[ind].append(int(temp[2]))
        elif len(temp) == 4:
            adj[ind].append(int(temp[2]))
            adj[ind].append(int(temp[3]))
    print(adj,vals)
    sunhwa(1)
    print('#{} {}'.format(tc,ans))