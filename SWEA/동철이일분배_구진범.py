T = int(input())
for t in range(1,2):
    n=int(input())
    m=1<<n
    d=[0]*m
    #입력받은 수들에 각 0.01곱해서 저장
    p=[[*map(lambda x:x*.01,map(int,input().split()))]for _ in range(n)]
    print(p)
    d[0]=1
    for i in range(m):
        print('i: ', i)
        #i를 이진법으로 바꾸고 1의 개수를 세어줌
        x=bin(i).count('1')
        print('x: ', x)
        for j in range(n):
            #j만큼1을 shift한 곳과 i의 비트 둘다 1이어야지만 1! 아니면 0
            if(1<<j)&i==0:
                #print(j,i)
                #와...진짜......이해안감...0.....대박.이다...이분 천재다...ㅠ
                print(f'd[{i|(1<<j)}]', f'max(d[{i|(1<<j)}],d[{i}]*p[{x}][{j}]')
                d[i|(1<<j)]=max(d[i|(1<<j)],d[i]*p[x][j])
        print(d)
    #d마지막 값에 저장된 것을 소수점 6째까지 표신
    print(f'#{t+1} {d[-1]*100:.6f}')