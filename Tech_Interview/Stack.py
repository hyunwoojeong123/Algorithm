class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    #push
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    #pop
    def pop(self):
        if self.is_empty():
            return -1
        data = self.top.data
        self.top = self.top.next
        return data

    #is_empty
    def is_empty(self):
        if self.top:
            return False
        else:
            return True

    #top
    def top_data(self):
        if self.is_empty():
            return -1
        return self.top.data

st = Stack()
st.push(1)
st.push(2)
st.push(3)
print(st.pop())
print(st.top_data())
print(st.pop())
print(st.top_data())