class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Use monotonic stack
        res = [0] * len(temperatures)
        stack = [] # [temp, index]

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t: # Compare top of stack with current temp
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([t,i])
        return res        
