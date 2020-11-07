## Linked List
# append
# getDataIndex
# insertNodeatIndex
# insertNodeatData
# deleteAtIndex
# clear
# print

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    
    def push(self,node):
        if self.head == None:
            self.head = node
        else:
            nextn = self.head
            self.head = node
            self.head.next = nextn

    def append(self,node):
        if self.head == None:
            self.head = node
        else:
            curn = self.head
            while curn.next != None:
                curn = curn.next
            curn.next = node

    def getDataIndex(self,data):
        curn = self.head
        idx = 0
        while curn:
            if curn.data == data:
                return idx
            idx += 1
            curn = curn.next
        return -1
    
    def insertNodeAtIndex(self,idx,node):
        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node
        else:
            curn = self.head
            prevn = None
            cur_i = 0
            while cur_i < idx:
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                prevn.next = node
                node.next = curn
            else:
                return -1
    
    def insertNodeAtData(self,data,node):
        # Data를 찾았을 때와 못찾을 때를 구분해야함
        # 찾으면 그 data의 앞에 넣는 걸로 하자
        idx = self.getDataIndex(data)
        if idx >= 0:
            self.insertNodeAtIndex(idx,node)
        else:
            return -1

    def deleteAtIndex(self,idx):
        cur_i = 0
        curn = self.head
        prevn = None
        nextn = self.head.next
        if idx == 0:
            self.head = nextn
        else:
            while cur_i < idx:
                if curn.next:
                    prevn = curn
                    curn = nextn
                    nextn = nextn.next
                else:
                    break
                cur_i += 1
            if cur_i != idx:
                return -1
            else:
                prevn.next = nextn
    
    def clear(self):
        self.head = None

    def print(self):
        curn = self.head
        string = ''
        while curn:
            string += str(curn.data)
            curn = curn.next
            if curn:
                string += '->'
        print(string)


lst = LL()
lst.push(Node(1))
lst.push(Node(2))
lst.append(Node(3))
lst.append(Node(4))
lst.deleteAtIndex(2)
lst.insertNodeAtData(1,Node(10))
lst.insertNodeAtIndex(2,Node(13))
lst.print()
lst.clear()
lst.print()