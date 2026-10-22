class ArrayQueue:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.front = 0
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == len(self.data)
    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow")
        rear = (self.front + self.size) % len(self.data)
        self.data[rear] = value
        self.size += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        value = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value
    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.data[self.front]
    def __str__(self):
        if self.is_empty():
            return "Queue: [empty]"
        items = []
        for i in range(self.size):
            idx = (self.front + i) % len(self.data)
            items.append(str(self.data[idx]))
        return "Queue (front to rear): " + " -> ".join(items)