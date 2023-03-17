class Solution:
    def isValid(self, s: str) -> bool:
       brackets = {')':'(', ']':'[','}':'{'}
       stack = []

       for c in s:
           if c in brackets:
               # Open brackets already inside stack
               if stack and stack[-1] == brackets[c]: 
                   # check stack not empty and the last item inside stack
                   # is an open bracket of same type as c
                   stack.pop()
                   # Remove               
               else: 
                    return False
           else: stack.append(c) # Add open brackets to stack
       return not stack   