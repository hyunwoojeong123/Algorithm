from pprint import pprint
visited, arr, N, ans, ans_num = [], [], -1, 0 , -1
di = [0,0,1,-1]
dj = [1,-1,0,0]

def BFS():
    global visited,ans,ans_num
    for i in range(N):
        for j in range(N):
            visited = [[0 for x in range(N)] for y in range(N)]
            q = []
            q.append([i,j])
            while len(q) > 0:
                pi,pj = q.pop(0)
                for k in range(4):
                    ni = pi + di[k]
                    nj = pj + dj[k]

                    if ni < 0 or nj < 0 or ni >= N or nj >= N:
                        continue
                    print(f'{arr[ni][nj]} 로 갈려함')
                    if arr[ni][nj] - 1 != arr[i][j]:
                        print('근데 못감')
                        continue
                    q.append([ni,nj])
                    visited[ni][nj] = visited[pi][pj] + 1
            max_len = 0
            print(arr[i][j])
            pprint(visited)
            for k in range(N):
                for l in range(N):
                    max_len = max(max_len,visited[k][l])
            if max_len > ans:
                ans = max_len
                ans_num = arr[i][j]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for x in range(N)]
    ans_num, ans = -1,0
    BFS()
    print(f'#{tc} {ans_num} {ans}')
