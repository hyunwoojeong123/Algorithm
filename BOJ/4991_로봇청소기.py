while True:
    w,h = map(int,input().split())
    if w== 0 and h==0:
        break
    bang = []
    for _ in range(h):
        bang.append(input())
    #