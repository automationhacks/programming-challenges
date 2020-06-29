class Node:
    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        if self.size >= self.capacity:
            return False

        self.size += 1
        node = Node(value)

        if self.size == 1:
            self.bottom = node

        self.join(node, self.top)
        self.top = node
        return True

    def pop(self):
        if not self.top:
            return None

        top = self.top
        self.top = self.top.below
        self.size -= 1
        return top.value

    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    def remove_bottom(self):
        bottom = self.bottom
        self.bottom = self.bottom.above

        if self.bottom:
            self.bottom.below = None

        self.size -= 1
        return bottom.value


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, value):
        last = self.get_last_stack()
        if last and not last.is_full():
            last.push(value)
        else:
            stack = Stack(self.capacity)
            stack.push(value)
            self.stacks.append(stack)

    def pop(self):
        last = self.get_last_stack()

        if not last:
            return None

        value = last.pop()
        if last.size == 0:
            del self.stacks[-1]
        return value

    def pop_at(self, index):
        return self.left_shift(index, True)

    def get_last_stack(self):
        if not self.stacks:
            return None
        return self.stacks[-1]

    def left_shift(self, index, remove_top):
        stack = self.stacks[index]
        removed_item = stack.pop() if remove_top else stack.remove_bottom()

        if stack.is_empty():
            del self.stacks[index]
        elif len(self.stacks) > index + 1:
            value = self.left_shift(index + 1, False)
            stack.push(value)
        return removed_item


def test_set_of_stacks():
    stacks = SetOfStacks(5)

    for i in range(35):
        stacks.push(i)

    popped = []
    for _ in range(35):
        popped.append(stacks.pop())

    assert popped == list(reversed(range(35)))


def test_set_of_stacks_pop_at():
    stacks = SetOfStacks(5)

    for i in range(35):
        stacks.push(i)

    popped = []
    for _ in range(31):
        popped.append(stacks.pop_at(0))

    assert popped == list((range(4, 35)))
