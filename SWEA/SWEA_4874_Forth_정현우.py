T = int(input())
for tc in range(1,T+1):
    flag = False
    data = list(input().split())
    N = len(data)
    stack = []
    for i in range(N-1):
        #print(d)
        if data[i].isdigit():
            stack.append(data[i])
        else:
            try:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if data[i] == '+':
                    stack.append(str(num1+num2))
                if data[i] == '-':
                    stack.append(str(num1-num2))
                if data[i] == '*':
                    stack.append(str(num1*num2))
                if data[i] == '/':
                    stack.append(str(num1//num2))
            except:
                flag = True
    if not flag and len(stack) == 1:
        print('#{} {}'.format(tc,stack[0]))
    elif flag  or len(stack) > 1:
        print('#{} error'.format(tc))
