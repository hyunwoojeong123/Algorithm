dy = [0,-1,0,1]
dx = [1,0,-1,0]

def rotate(lst):
    res = []
    for each in lst:
        res.append(each)
    ex,ey = lst.pop()
    while lst:
        x,y = lst.pop()
        diff_x,diff_y = ex-x,ey-y
        nx,ny = ex+diff_y,ey-diff_x
        res.append([nx,ny])
    return res

def dc(x,y,d,g):
    if g == 0:
        return [[x,y],[x+dx[d],y+dy[d]]]
    return dc(x,y,d,g-1) + rotate(dc(x,y,d,g-1))

N = int(input())
arr = [[False for j in range(101)] for i in range(101)]
for _ in range(N):
    x,y,d,g = map(int,input().split())
    for (xx,yy) in dc(x,y,d,g):
        arr[xx][yy] = True
ans = 0
for i in range(100):
    for j in range(100):
       if arr[i][j] and arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1]:
           ans += 1

# for i in range(10):
#     for j in range(10):
#         print(arr[i][j], end=' ')
#     print()
print(ans)