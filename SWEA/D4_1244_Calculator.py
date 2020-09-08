isp = {'*' : 2, '+' : 1, '(' : 0}
icp = {'*' : 2, '+' : 1, '(' : 3}

for tc in range(1,11):
    sik_len = int(input())
    sik = input()
    huwi_sik = ''
    opers = []
    # 식을 후위 표기법으로 변환
    for char in sik:
        #print(char)
        #print('변환')
        if ord(char) >= ord('0') and ord(char) <= ord('9'):
            huwi_sik += char
        elif char == ')':
            while opers:
                if opers[-1] == '(':
                    opers.pop()
                    break
                huwi_sik += opers.pop()
        else:
            while opers and not icp[char] > isp[opers[-1]]:
                huwi_sik += opers.pop()
            opers.append(char)
        #print(huwi_sik)
    while opers:
        huwi_sik += opers.pop()

    #print(huwi_sik)
    # 후위식을 계산
    result = 0
    stack = []
    for each in huwi_sik:
        if ord(each) >= ord('0') and ord(each) <= ord('9'):
            stack.append(int(each))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if each == '+':
                stack.append(num1+num2)
            else:
                stack.append(num1*num2)
    result = stack[0]
    print('#{} {}'.format(tc,result))

