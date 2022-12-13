from MinQueue.MinStack import MinStack

class MinQueue:
    def __init__(self):
        self.f = MinStack()
        self.r = MinStack()

    def min(self):
        a = self.f.min()
        b = self.r.min()
        if not a:
            if not b:
                return None
            return b
        if not b:
            return a
        return min(a,b)

    def print(self):
        print(self.f.print() + " | " + self.r.print() + " | Queue Min: " + str(self.min()))

    def enqueue(self, val):
        self.f.push(val=val)

    def dequeue(self):
        if self.r.is_empty():
            while not self.f.is_empty():
                self.r.push(self.f.pop())
        return self.r.pop()