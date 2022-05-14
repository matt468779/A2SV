class Solution:
    memo = [0, 1] + [-1]*29
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return self.memo[n]
        elif self.memo[n] != -1:
            return self.memo[n]
        self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]