ops = ['+', '-', '*', '//']

min_val = 1000000001
max_val = -1000000001

def permute(i,num):
    global max_val,min_val
    backup = num
    if i == N-1:
        if max_val < num:
            max_val = num
        if min_val > num:
            min_val = num
        return
    for k in range(4):
        if operator_cnt[k] != 0:
            operator_cnt[k] -= 1
            if i == 0:
                if k == 0:
                    num = A[i] + A[i+1]
                if k == 1:
                    num = A[i] - A[i+1]
                if k == 2:
                    num = A[i] * A[i+1]
                if k == 3:
                    if A[i] < 0:
                        num = -(abs(A[i])//A[i+1])
                    else:
                        num = A[i] // A[i+1]
            else:
                if k == 0:
                    num += A[i+1]
                if k == 1:
                    num -= A[i+1]
                if k == 2:
                    num *= A[i+1]
                if k == 3:
                    if num < 0:
                        num = -(abs(num)//A[i+1])
                    else:
                        num = num // A[i+1]
            permute(i+1,num)
            operator_cnt[k] += 1
            num = backup


N = int(input())
A = list(map(int,input().split()))
operator_cnt = list(map(int,input().split()))
permute(0,0)
print(max_val)
print(min_val)
