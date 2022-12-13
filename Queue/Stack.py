from Queue.Node import Node

class Stack:
    def __init__(self) -> None:
        self.head = Node()

    def is_empty(self):
        return not self.head.next
    
    def push(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    def pop(self):
        if not self.is_empty():
            val = self.head.next.val
            self.head.next = self.head.next.next
            return val
        return None

    def print(self):
        s = "["
        aux = self.head.next
        while aux:
            s += str(aux.val) + ", "
            aux = aux.next
        if self.head.next:
            s = s[:-2]
        s += "]"
        return s
            