class MultiStack:
    def __init__(self, stack_size, num_stacks=3):
        self.stack_size = stack_size
        self.num_stacks = num_stacks

        self.stack = [0] * stack_size * num_stacks
        self.sizes = [0] * num_stacks

    def push(self, item, stack_num):
        if self.is_full(stack_num):
            raise Exception('Stack is full')

        self.sizes[stack_num] += 1
        self.stack[self.index_of_top(stack_num)] = item

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Stack is empty')

        value = self.stack[self.index_of_top(stack_num)]
        self.stack[self.index_of_top(stack_num)] = 0
        self.sizes[stack_num] -= 1

        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Stack is empty')
        return self.stack[self.index_of_top(stack_num)]

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size


def test_multi_stack():
    multi_stack = MultiStack(2)
    print()
    assert multi_stack.is_empty(1) is True

    multi_stack.push(2, 1)
    assert multi_stack.peek(1) == 2
    assert multi_stack.is_empty(1) is False

    multi_stack.push(4, 1)
    assert multi_stack.peek(1) == 4

    multi_stack.pop(1)
    assert multi_stack.peek(1) == 2

    multi_stack.push(9, 2)
    assert multi_stack.peek(2) == 9


