from random import randint

from python.cracking_the_coding_interview.ch_03_stacks_and_queues.Stack import Stack


class SortedStack:
    def __init__(self):
        self.stack = Stack()
        self.temp = Stack()

    def push(self, item):
        top = self.stack.peek()
        if top is None:
            self.stack.push(item)
            return

        if item <= top:
            self.stack.push(item)
        else:
            while not self.stack.is_empty():
                if item > self.stack.peek():
                    self.temp.push(self.stack.pop())
                else:
                    break

            self.stack.push(item)
            while not self.temp.is_empty():
                self.stack.push(self.temp.pop())

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        self.stack.pop()


def test_sorted_stack():
    sorted_stack = SortedStack()

    for i in range(20):
        random = randint(5, 100)
        print(f'Inputting: {random}')
        sorted_stack.push(random)

    print(sorted_stack.stack.items)

