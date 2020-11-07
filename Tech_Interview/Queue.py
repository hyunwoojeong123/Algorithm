class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    #enqueue
    def enqueue(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    #dequeue
    def dequeue(self):
        if self.head == None:
            return -1
        else:
            v = self.head.data
            self.head = self.head.next

            if self.head == None:
                self.tail = None
            return v

    #print
    def print(self):
        string = ''
        curn = self.head
        while curn:
            string += str(curn.data)
            if curn.next != None:
                string += '->'
            curn = curn.next
        print(string)

q = Queue()
q.enqueue(Node(1))
q.enqueue(Node(2))
q.enqueue(Node(3))
q.dequeue()
q.print()