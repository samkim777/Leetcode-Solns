class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Compare with minimum in stack, and append accordingly
        if self.minStack:
            cur = self.minStack[-1]
            self.minStack.append(min(cur, val))
        else:
            self.minStack.append(val)    

    def pop(self) -> None:
        self.stack.pop() # Removes top of stack
        self.minStack.pop() # removes top of stack

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # O(1) time complexity for each
        # If empty, just add onto stack
        # Keep track of minimum value seen so far
        # For example, when stack has [-2] and we add -3,
        # our minimum is now -3, and stack is [-3,-2]
        # if we now add 0, minimum is -3, stack is [0,-3,-2]
        # We have two stacks, one where we keep track of numbers being added,
        # and another stack that keeps track of minimum seen so far
        # When we pop, pop from both, and that would be O(1) time complexity
        # What if empty?, will be called on non-empty stacks
        return self.minStack[-1]
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()