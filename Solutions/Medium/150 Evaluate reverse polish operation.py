class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # First thing is how to check +,-,*,/? 
        # Test each case by checking if +, then add, etc..
        # ["2","1","+","3","*"] is (2 + 1) * 3
        # Using stacks: Put everything into stack
        # If we've got an operator, replace the last 2 numerical values
        # with the number1 operand number2 value
        # Expect we won't have empty lists
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop()) # Pop the first two numbers
            elif c == '-':
                a,b = stack.pop(),stack.pop()
                stack.append(b - a) 
            elif c == '*':
                stack.append( stack.pop() * stack.pop())
            elif c == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a)) 
            else: 
                stack.append(int(c)) # Number    
        return stack[0] 