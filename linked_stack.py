class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedStack:
    def __init__(self):
        self.top = None
    def is_empty(self):
        return self.top is None
    def is_full(self):
        return False
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        value = self.top.value
        self.top = self.top.next
        return value
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.value
    def __str__(self):
        if self.is_empty():
            return "Stack: [empty]"
        curr = self.top
        vals = []
        while curr:
            vals.append(str(curr.value))
            curr = curr.next
        return "Stack (top to bottom): " + " -> ".join(vals)