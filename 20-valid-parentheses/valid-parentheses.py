class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(', ']':'[', '}':'{'}

        for b in s:
            if b not in brackets:
                stack.append(b)
            else:
                if stack and stack[-1] == brackets[b]:
                    stack.pop()
                else:
                    return False
        return not stack                