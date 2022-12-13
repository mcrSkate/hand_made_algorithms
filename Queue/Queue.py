from Queue.Stack import Stack

class Queue:

    def __init__(self):
        self.f = Stack()
        self.r = Stack()

    def enqueue(self, val):
        self.f.push(val=val)

    def dequeue(self):
        if self.r.is_empty():
            while not self.f.is_empty():
                self.r.push(self.f.pop())
        return self.r.pop()

    def print(self):
        print("Front: " + self.f.print() + " Rear: " + self.r.print())