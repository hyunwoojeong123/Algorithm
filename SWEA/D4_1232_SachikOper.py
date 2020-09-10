def operate(i):
    if vals[i].isdigit():
        return int(vals[i])
    else:
        left,right = int(childrens[i][0]), int(childrens[i][1])
        if vals[i] == '-':
            return operate(left) - operate(right)
        elif vals[i] == '+':
            return operate(left) + operate(right)
        elif vals[i] == '/':
            return operate(left) / operate(right)
        elif vals[i] == '*':
            return operate(left) * operate(right)

for tc in range(1,11):
    N = int(input())
    childrens = [[] for _ in range(N+1)]
    vals = ['' for _ in range(N+1)]
    for _ in range(N):
        el = input().split()
        if len(el) == 4:
            # 요소가 연산자
            i,val,left,right = el[0], el[1], el[2], el[3]
            i = int(i)
            vals[i] = val
            childrens[i].append(left)
            childrens[i].append(right)
        if len(el) == 2:
            i,val = el[0],el[1]
            i = int(i)
            vals[i] = val
    print('#{} {}'.format(tc,int(operate(1))))