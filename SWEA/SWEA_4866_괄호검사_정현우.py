T = int(input())
for tc in range(1,T+1):
    sen = input()
    gwalho = []
    ans = -1
    for char in sen:
        #print(char,gwalho)
        if char == '{' or char == '(':
            gwalho.append(char)
        elif char == '}':
            if len(gwalho) == 0 or gwalho[len(gwalho)-1] != '{':
                ans = 0
                break
            else:
                gwalho.pop()
        elif char == ')':
            if len(gwalho) == 0 or gwalho[len(gwalho)-1] != '(':
                ans = 0
                break
            else:
                gwalho.pop()
    else:
        if len(gwalho) == 0:
            ans = 1
        else:
            ans = 0
    print('#{} {}'.format(tc,ans))
