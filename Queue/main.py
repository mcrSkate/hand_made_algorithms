from Queue.Queue import Queue

q = Queue()

q.print()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.print()
q.dequeue()
q.print()
q.dequeue()
q.print()
q.enqueue(4)
q.print()
q.enqueue(5)
q.dequeue()
q.print()
q.dequeue()
q.print()