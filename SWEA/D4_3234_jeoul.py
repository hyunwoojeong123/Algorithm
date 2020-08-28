def swap(Arr,a,b):
    temp = Arr[a]
    Arr[a] = Arr[b]
    Arr[b] = temp

def Permutation(Arr,Start,End):
    if Start == End:
        for _ in Arr:
            print( _, end = ' ')
        print('')
    else:
        for i in range(Start,End+1):
            swap(Arr,Start,i)
            Permutation(Arr,Start+1,End)
            swap(Arr,Start,i)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    chus = list(map(int,input().split()))
    Permutation(chus,0,len(chus)-1)

