T = int(input())

for tc in range(1, T+1):
    Data = list(map(int, input().split()))
    flag = False
    cnt = 0
    for index in range(6, 13, 2):
        result = []
        for i in range(2):
            Deck = [Data[x] for x in range(i, index,2)]
            cnt_lst = [0] * 12

            for j in range(len(Deck)):
                cnt_lst[Deck[j]] += 1

            k = 0
            Tri = Run = 0
            while k < 10:
                if cnt_lst[k] >= 3:
                    cnt_lst[k] -= 3
                    Tri += 1
                    continue

                if cnt_lst[k] >= 1 and cnt_lst[k + 1] >= 1 and cnt_lst[k + 2] >= 1:
                    cnt_lst[k] -= 1
                    cnt_lst[k + 1] -= 1
                    cnt_lst[k + 2] -= 1
                    Run += 1
                    continue
                k += 1

            cnt += 1

            if Tri > 0 or Run > 0:
                result.append(1)
            else:
                result.append(0)


        if (result[0] == 1 and result[1] == 1) or (result[0] == 2 and result[1] == 2) :
            flag = True
            print('#{} {}'.format(tc,1))
            break

        elif result[0] > result[1]:
            flag = True
            print('#{} {}'.format(tc,1))
            break

        elif result[0] < result[1]:
            flag = True
            print('#{} {}'.format(tc,1))
            break


    if flag:
        continue
    else:
        print('#{} {}'.format(tc,0))
