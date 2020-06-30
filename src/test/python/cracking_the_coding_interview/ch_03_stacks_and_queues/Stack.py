class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        else:
            return self.items.pop()

    def __len__(self):
        return len(self.items)

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            return None


    def is_empty(self):
        return self.items == []
