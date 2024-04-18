from collections import deque
from queue import Empty

class Queue:
    def __init__(self):
        self.items = deque()
    def is_empty (self):
        return len (self.items) == 0
    def enqueue (self, item):
        self.items.append (item)
    def dequeue (self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            return "Queue is Empty"
    def size(self):
        return len(self.items)

queue = Queue()

a = int(input("Number of numbers in Queue: "))
for x in range (0, a):
    b = int(input("Items: "))
    queue.enqueue(b)

print("Queue: ", list(queue.items))
print("Dequeue: ", queue.dequeue())
print("Queue after dequeueing: ", list(queue.items))
print("Dequeue: ", queue.dequeue())
print("Queue after dequeueing: ", list(queue.items))