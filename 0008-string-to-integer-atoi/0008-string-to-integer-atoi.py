
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        i = 0
        n = len(s)

        # Step 1: Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check the sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: Read digits and build the number
        result = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # Step 4: Check overflow before multiplying by 10
            if result > INT_MAX // 10 or (
                result == INT_MAX // 10 and digit > 7
            ):
                return INT_MIN if sign == -1 else INT_MAX

            result = result * 10 + digit
            i += 1

        return result * sign
