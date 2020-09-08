T = int(input())
for tc in range(1,T+1):
    info = input()
    N = len(info)
    flag = False
    ans = ''
    cards = {'S' : [], 'D' : [], 'H' : [], 'C' : []}
    for i in range(0,N,3):
        muni = info[i]
        num = info[i+1:i+3]
        if num in cards[muni]:
           ans = 'ERROR'
           flag = True
           break
        else:
            cards[muni].append(num)
    if not flag:
        ans = str(13-len(cards['S'])) + ' ' + str(13-len(cards['D'])) + ' ' + str(13-len(cards['H'])) + ' ' +str(13-len(cards['C']))
    print('#{} {}'.format(tc,ans))
