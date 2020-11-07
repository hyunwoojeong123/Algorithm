class Heap:
    def __init__(self):
        self.heap = [0]

    def heapify_upward(self):
        n = len(self.heap)-1
        while n > 1:
            p = n//2
            if self.heap[p] < self.heap[n]:
                self.heap[p],self.heap[n] = self.heap[n],self.heap[p]
                n = p
            else:
                break

    def heapify_downward(self):
        N = len(self.heap)
        n = 1
        while n < N:
            l, r = n * 2, n * 2 + 1
            if r >= N:
                break
            #print(n,l,r)
            if self.heap[n] < self.heap[l] or self.heap[n] < self.heap[r]:
                if self.heap[l] >= self.heap[r]:
                    self.heap[l],self.heap[n] = self.heap[n],self.heap[l]
                    n = l
                else:
                    self.heap[r],self.heap[n] = self.heap[n],self.heap[r]
                    n = r
            else:
                break

    def add(self, value):
        self.heap.append(value)
        self.heapify_upward()

    def delete(self):
        self.heap[1],self.heap[-1] = self.heap[-1],self.heap[1]
        res = self.heap.pop()
        self.heapify_downward()
        return res

    def is_empty(self):
        if len(self.heap) == 1:
            return True
        else:
            return False

    def print(self):
        print(self.heap)

hp = Heap()
# 힙소트
# 1. 배열에 잇는애들 다 힙에 넣는다.
# 2. 한 개씩 빼면서 배열 뒤부터 채운다.
arr = [7,6,5,4,3,2,1]
for each in arr:
    hp.add(each)
i = len(arr)-1
while not hp.is_empty():
    arr[i] = hp.delete()
    hp.print()
    print('arr[{}] = {}'.format(i,arr[i]))
    i -= 1
print(arr)