class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n = 3 ((())), (()()), (())(),()(())  (()())
        # n = 1 ()
        # We create 2 stacks of size n
        # One only has open brackets, the other closed
        # Each bracket can be surrounded by n - 1, n - 2,... 0 brackets
        # n = 2 (()) (()) (()
        stack = []
        res = []

        def backtrack(openN,closedN):
            if openN == closedN == n:
                res.append(''.join(stack))

            if openN < n:
                stack.append('(')
                backtrack(openN+1,closedN)
                stack.pop()

            if closedN < openN:
                stack.append(')')
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        return res   