def heapify(i):
    if i == 0:
        return
    parent = i // 2
    if heap[parent] < heap[i]:
        return
    heap[parent],heap[i] = heap[i],heap[parent]
    heapify(parent)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    heap = [0]
    idx = 0
    elements = list(map(int,input().split()))
    for element in elements:
        heap.append(element)
        idx += 1
        heapify(idx)
    sum = 0
    while idx > 0:
        idx //= 2
        sum += heap[idx]
    print('#{} {}'.format(tc,sum))