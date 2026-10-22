class ArrayStack:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.top = -1
    def is_empty(self):
        return self.top == -1
    def is_full(self):
        return self.top == len(self.data) - 1
    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow")
        self.top += 1
        self.data[self.top] = value
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        value = self.data[self.top]
        self.top -= 1
        return value
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data[self.top]
    def __str__(self):
        if self.is_empty():
            return "Stack: [empty]"
        elements = [str(self.data[i]) for i in range(self.top, -1, -1)]
        return "Stack (top to bottom): " + " -> ".join(elements)