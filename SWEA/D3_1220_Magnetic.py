import sys
sys.stdin = open("input.txt","r")


for tc in range(1,11):
    N = int(input())
    board = [list(map(int,input().split())) for i in range(N)]
    # 1: N극
    # 2: S극
    # 위가 N극 아래가 S극
    #print(N,board)
    ans = 0
    for j in range(N):
        stack = []
        # 스택 왼쪽 : N극, 오른쪽: S극
        for i in range(N):
            if board[i][j] != 0:
                stack.append(board[i][j])
        # 오른쪽 바닥으로 떨어지는 넘들 처리
        while stack[-1] == 1:
            stack.pop()
        # 왼쪽 바닥으로 떨어지는 넘들 처리
        while stack[0] == 2:
            stack.pop(0)
        # 교착 상태 확인
        while stack:

            magnet = stack.pop()
            opp_magnet = -1
            if magnet == 1:
                opp_magnet = 2
            else:
                opp_magnet = 1
            # 같은 극인애 다 팝함
            while stack:
                if stack[-1] == magnet:
                    stack.pop()
                else:
                    break
            # 다른 극인애 다 팝함
            while stack:
                if stack[-1] == opp_magnet:
                    stack.pop()
                else:
                    break
            # 교착상태 한개 체크
            ans += 1
    print('#{} {}'.format(tc,ans))

