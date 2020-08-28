T = int(input())
for tc in range(1,T+1):
    A = input()
    B = input()
    ans = 0
    len_A,len_B = len(A),len(B)
    for i in range(len_B-len_A+1):
        for j in range(len_A):
            if A[j] != B[i+j]:
                break
        else:
            ans = 1
            break
    print(f'#{tc} {ans}')
