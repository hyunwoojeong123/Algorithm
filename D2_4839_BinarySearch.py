def binary_search(find_p,total_p):
    cnt = 0
    l = 1
    r = total_p
    c = int((l+r)/2)
    while(l <= r):
        #print(l,r,c,cnt)
        if c == find_p:
            return cnt
        cnt += 1
        if find_p < c:
            r = c
        else:
            l = c
        c = int((l+r)/2)


T = int(input())
for tc in range(1,T+1):
    P,A,B = list(map(int,input().split()))
    #print(P,A,B)
    A_cnt = binary_search(A,P)
    B_cnt = binary_search(B,P)
    if A_cnt == B_cnt:
        print(f'#{tc} 0')
    elif A_cnt < B_cnt:
        print(f'#{tc} A')
    else:
        print(f'#{tc} B')