class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()   # r - c
        diag2 = set()   # r + c

        def backtrack(r):
            # All queens placed
            if r == n:
                ans.append(["".join(row) for row in board])
                return

            for c in range(n):
                # Check column and diagonals
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue

                # Place queen
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                # Move to next row
                backtrack(r + 1)

                # Undo / Backtrack
                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return ans