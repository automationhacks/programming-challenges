import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()

    def push(self, item):
        current_min = self.min()
        if item <= current_min:
            self.min_stack.push(item)

        super().push(item)

    def pop(self):
        value = super().pop()
        if value == self.min():
            self.min_stack.pop()
        return value

    def min(self):
        if self.min_stack.is_empty():
            return sys.maxsize
        else:
            return self.min_stack.peek()


def test_min_stack():
    items = [2, 5, 1, 6]
    stack = MinStack()
    for item in items:
        stack.push(item)

    value = stack.pop()
    assert value == 6
    assert stack.min() == 1

    value = stack.pop()
    assert value == 1
    assert stack.min() == 2
