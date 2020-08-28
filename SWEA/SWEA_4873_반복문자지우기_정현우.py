T = int(input())
for tc in range(1,T+1):
    sen = input()
    while True:
        flag = False
        for i in range(0,len(sen)-1):
            if sen[i] == sen[i+1]:
                flag = True
                temp = sen[:i] + sen[i+2:]
                sen = temp
                break

        #print(sen)
        if not flag:
            break
    print('#{} {}'.format(tc,len(sen)))