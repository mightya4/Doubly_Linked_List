#Create Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next, self.prev = None, None