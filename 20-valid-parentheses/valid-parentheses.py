class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {')' : '(', ']' : '[', '}': '{'}
        if len(s) <= 1:
            return False
        for bracket in s:
            if not stack and bracket in chars:
                return False
            if bracket not in chars: # open
                stack.append(bracket)
            else:
                if stack and stack[-1] != chars[bracket]:
                    return False
                if stack and stack[-1] == chars[bracket]:
                    stack.pop()    
        return not stack        