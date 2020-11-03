"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Example 1:

Input ["MinStack","push","push","push","getMin","pop","top","getMin"] [[],[-2],[0],[-3],[],[],[],[]]

Output [null,null,null,null,-3,null,0,-2]

Explanation MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0);
minStack.push(-3); minStack.getMin(); // return -3 minStack.pop(); minStack.top(); // return 0
minStack.getMin(); // return -2

Constraints:

    Methods pop, top and getMin operations will always be called on non-empty stacks.
"""


# Time Complexity : O(1) for all operations.
#
# push(...): Checking the top of a Stack, comparing numbers, and pushing to the top of a Stack (or
# adding to the end of an Array or List) are all O(1) operations. Therefore, this overall is an O(1)
# operation.
#
# pop(...): Popping from a Stack (or removing from the end of an Array, or List) is an O(1) operation.
#
# top(...): Looking at the top of a Stack is an O(1) operation.
#
# getMin(...): Same as above. This operation is O(1) because we do not need to compare values to find
# it. If we had not kept track of it on the Stack, and instead had to search for it each time, the
# overall time complexity would have been O(n).
#
# Space Complexity : O(n).
#
# Worst case is that all the operations are push. In this case, there will be O(2n) = O(n) space used


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, num: int) -> None:
        # if stack is empty, add num itself as min
        if not self.stack:
            self.stack.append((num, num))
            return

        current_num, current_min = self.peek()
        self.stack.append((num, min(num, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.peek()[0]

    def getMin(self) -> int:
        return self.peek()[1]

    def peek(self):
        return self.stack[-1]


def test_stack_operations_on_positive():
    # push and pop
    obj = MinStack()
    obj.push(5)
    obj.pop()

    # top
    obj.push(10)
    obj.push(7)
    obj.push(8)
    last_value = obj.top()
    assert last_value == 8

    # getMin
    minimum = obj.getMin()
    assert minimum == 7


def test_stack_operations_on_negative():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    assert stack.getMin() == -3
    assert stack.top() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.getMin() == -2
