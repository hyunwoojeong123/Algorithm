def operate(i):
    e = elements[i]
    if e.isdigit():
        return int(e)
    else:
        L,R = childs[i][0], childs[i][1]
        if e == '+':
            return operate(L) + operate(R)
        if e == '-':
            return operate(L) - operate(R)
        if e == '*':
            return operate(L) * operate(R)
        if e == '/':
            return operate(L) / operate(R)

for tc in range(1,11):
    N = int(input())
    elements = ['' for _ in range(N+1)]
    childs = [[] for _ in range(N+1)]

    for i in range(1,N+1):
        temp = input().split()
        node = int(temp[0])
        element = temp[1]
        child = []
        if len(temp) == 4:
            child.append(int(temp[2]))
            child.append(int(temp[3]))
        elements[node] = element
        childs[node] = child
    # print(elements)
    # print(childs)
    print('#{} {}'.format(tc,int(operate(1))))