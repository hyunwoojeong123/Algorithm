T = int(input())
for tc in range(1,T+1):
    A = input()
    B = input()
    ans = -1
    for i in range(len(A)):
        cnt = 0
        for j in range(len(B)):
            if A[i] == B[j]:
                cnt += 1
        if cnt > ans: ans = cnt
    print(f'#{tc} {ans}')