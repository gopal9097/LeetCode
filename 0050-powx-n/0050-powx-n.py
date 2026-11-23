class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = abs(n)
        result = 1.0
        base = x

        while m > 0:
            if m & 1:
                result *= base
            base *= base
            m >>= 1

        return 1.0 / result if n < 0 else result