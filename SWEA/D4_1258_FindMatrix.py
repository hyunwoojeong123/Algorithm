T = int(input())
for tc in range(1,T+1):
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(int,input().split())))
    visited = [[False for x in range(0,n)]for y in range(0,n)]
    Matrixes = []
    #행렬을 찾는다.
    for i in range(0,n):
        for j in range(0,n):
            if board[i][j] != 0 and not visited[i][j]:
                si,ei,sj,ej = i,i,j,j
                while ei < n:
                    if board[ei][j] == 0:
                        break
                    ei += 1
                while ej < n:
                    if board[i][ej] == 0:
                        break
                    ej += 1
                for ti in range(si,ei):
                    for tj in range(sj,ej):
                        visited[ti][tj] = True
                #print(f'행렬 찾음 ({si},{sj})')
                garo = ej-sj
                sero = ei-si
                nulbi = garo*sero
                #print(f'{garo} {sero}')
                Matrixes.append([nulbi,garo,sero])
    Matrixes = sorted(Matrixes,key=lambda Matrixes: Matrixes[0])
    print(f'#{tc} {len(Matrixes)}', end = ' ')
    for Matrix in Matrixes:
        print(f'{Matrix[2]} {Matrix[1]}', end = ' ')
    print('\n')