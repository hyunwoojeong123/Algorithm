N = int(input())
for i in range(1,N+1):
    str_i = str(i)
    cnt_369 = 0
    for each in str_i:
        if int(each) % 3 == 0 and int(each) != 0:
            cnt_369 += 1
    if cnt_369 == 0:
        print(i, end = ' ')
    else:
        print('-'*cnt_369, end = ' ')