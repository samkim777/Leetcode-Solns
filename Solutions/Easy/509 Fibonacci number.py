class Solution:
    def fib(self, n: int) -> int:

        # Define base case
        if n == 0:
            return 0
        elif n == 1:
            return 1    
        else:
            return self.fib(n-1) + self.fib(n-2)
     # n = 4 : f(3) + f(2) + f(1) + f(0)       
            