from python.cracking_the_coding_interview.ch_03_stacks_and_queues.Stack import Stack


class MyQueue:
    def __init__(self):
        self.new_stack = Stack()
        self.old_stack = Stack()

    def add(self, item):
        self.new_stack.push(item)

    def remove(self):
        while not self.new_stack.is_empty():
            item = self.new_stack.pop()
            self.old_stack.push(item)

        value = self.old_stack.pop()
        while not self.old_stack.is_empty():
            self.new_stack.push(self.old_stack.pop())

        return value


def test_my_queue():
    queue = MyQueue()
    test_data = [2, 5, 5, 7, 6]
    for data in test_data:
        queue.add(data)

    assert queue.remove() == 2
