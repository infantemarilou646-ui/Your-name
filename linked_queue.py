class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None
    def is_full(self):
        return False
    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value
    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.value
    def __str__(self):
        if self.is_empty():
            return "Queue: [empty]"
        curr = self.front
        vals = []
        while curr:
            vals.append(str(curr.value))
            curr = curr.next
        return "Queue (front to rear): " + " -> ".join(vals)
        