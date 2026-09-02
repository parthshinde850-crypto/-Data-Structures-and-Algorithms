# Queue

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self,x):
        if x == -1:
            return None
        else:
            return self.queue.append(x)
    
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow")
        else:
            return self.queue.popleft()
        
    def front(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            return self.queue[0]
        
    def display(self):
        print(self.queue)

q = Queue()

while True:
    x = int(input("Enter element to enqueue in queue:"))

    if x == -1:
        break

    q.enqueue(x)

q.display()

print("dequeue", q.dequeue())
print("front", q.front())

q.display()

