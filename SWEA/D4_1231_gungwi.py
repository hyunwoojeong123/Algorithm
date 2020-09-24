def inorder(i):
    if arr[i] == '':
        return
    left = i*2
    right = i*2+1
    inorder(left)
    print(arr[i], end='')
    inorder(right)

for tc in range(1,11):
    N = int(input())
    arr = ['' for _ in range(N*5)]
    for i in range(1,N+1):
        temp = input().split()
        node = int(temp[0])
        char = temp[1]
        arr[node] = char
    print('#{}'.format(tc), end = ' ')
    inorder(1)
    print()