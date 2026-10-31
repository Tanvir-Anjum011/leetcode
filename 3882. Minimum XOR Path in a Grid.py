class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                val = grid[i][j]

                if i == 0 and j == 0:
                    dp[j] = {val}
                    continue

                current = set()

                if i > 0:
                    for x in dp[j]:
                        current.add(x ^ val)

                if j > 0:
                    for x in dp[j - 1]:
                        current.add(x ^ val)

                dp[j] = current

        return min(dp[-1])