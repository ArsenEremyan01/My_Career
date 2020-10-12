class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)

    # while i < N:
    #     total = a1 + a2
    #     a1, a2 = a2, total
    #     i += 1
    # return a2