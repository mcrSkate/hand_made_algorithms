from MinQueue.MinNode import MinNode

class MinStack:
    def __init__(self):
        self.head = MinNode()

    def is_empty(self):
        return not self.head.next

    def push(self, val):
        node = MinNode(val=val)
        if not self.is_empty():
            if node.val > self.head.next.min.val:
                node.min = self.head.next.min
        node.next = self.head.next
        self.head.next = node

    def pop(self):
        if not self.is_empty():
            val = self.head.next.val
            self.head.next = self.head.next.next
            return val
        return None

    def min(self):
        return self.head.next.min.val if not self.is_empty() else None

    def print(self):
        s = "["
        aux = self.head.next
        while aux:
            s += str(aux.val) + ", "
            aux = aux.next
        if self.head.next:
            s = s[:-2]
        s += "]"
        val = self.min()
        return s + " Min: " + (str(val) if val else "None")