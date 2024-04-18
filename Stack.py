class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)

print("Stack:", stack.items)

popped = stack.pop()
print("Popped:", popped)

print("Stack:", stack.items)

top_element = stack.peek()
print("Top element:", top_element)

stack_size = stack.size()
print("Stack size:", stack_size)
