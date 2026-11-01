class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        n, m = len(haystack), len(needle)

        # Build LPS (Longest Prefix Suffix) array
        lps = [0] * m
        j = 0

        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = lps[j - 1]

            if needle[i] == needle[j]:
                j += 1

            lps[i] = j

        # KMP pattern matching
        i = j = 0

        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == m:
                    return i - j

            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1