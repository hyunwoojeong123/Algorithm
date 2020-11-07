class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    # append
    def append(self, node):
        if self.head:
            curn = self.head
            while curn.next:
                curn = curn.next
            curn.next = node
            node.prev = curn
        else:
            self.head = node

    # insertNodeAtIndex
    def insertNodeAtIndex(self,idx,node):
        prevn = None
        nextn = None

        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node

        else:
            cur_i = 0
            curn = self.head
            while cur_i < idx:
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                node.prev = prevn
                node.next = curn
                prevn.next = node
                if curn:
                    curn.prev = node
            else:
                return -1

    # getDataIndex
    def getDataIndex(self, data):
        curn = self.head
        cur_i = 0

        while curn:
            if curn.data == data:
                return cur_i
            curn = curn.next
            cur_i += 1
        return -1
    # insertNodeAtData
    def insertNodeAtData(self, data, node):
        index = self.getDataIndex(data)
        if index >= 0:
            self.insertNodeAtIndex(index, node)
        else:
            return -1

    # deleteAtIndex
    def deleteAtIndex(self, idx):
        nextn = None
        prevn = None
        cur_i = 0

        if idx == 0:
            if self.head:
                self.head = self.head.next
                self.head.prev = None
            else:
                return -1
        curn = self.head

        while cur_i < idx:
            if curn.next:
                prevn = curn
                curn = curn.next
                nextn = curn.next
            else:
                break
            cur_i += 1
        if cur_i == idx:
            if nextn:
                nextn.prev = prevn
            prevn.next = nextn
        else:
            return -1
    # print