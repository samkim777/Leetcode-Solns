class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    # one stack
    # Once length of operator stack is 1, we pop the two from numbers
    # and perform the operation then append to nums stack
        if len(tokens) == 1:
            return int(tokens[-1])

        numStack = []
        for s in tokens:
            if s == "*": # Handle the case here
                # Get the two numbers: Assume
                num1, num2 = numStack.pop(), numStack.pop()
                numStack.append(num1 * num2)
            elif s == "/":
                num1, num2 = numStack.pop(), numStack.pop()
                # num1 is not the most recent
                numStack.append(int(num2 / num1))
            elif s == "-":
                num1, num2 = numStack.pop(), numStack.pop()
                numStack.append(num2 - num1)
            elif s == "+":
                num1, num2 = numStack.pop(), numStack.pop()
                numStack.append(num2 + num1)
            else: #number
                numStack.append(int(s))    
        return numStack[-1]        