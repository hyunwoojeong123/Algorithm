ref = {'ZRO' : 0 , 'ONE' : 1 , 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

def change(str):
    return ref[str]

T = int(input())
for tc in range(1,T+1):
    num,N = input().split()
    N = int(N)
    words = list(input().split())
    words = sorted(words, lambda x: ref[x])
    print(f'#{tc}' , end = ' ')
    for i in range(N):
        print(words[i], end = ' ')
