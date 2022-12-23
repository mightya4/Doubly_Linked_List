#Create Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next, self.prev = None, None

class doubly_linked_list:
    def __init__(self):
        self.head = None

#Adding data elements
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode