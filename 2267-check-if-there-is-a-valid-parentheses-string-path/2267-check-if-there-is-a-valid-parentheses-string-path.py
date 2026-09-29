class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        @cache
        def dfs(i: int, j: int, balance: int) -> bool:
            balance += 1 if grid[i][j] == '(' else -1           
            if balance < 0 or balance > (m + n - i - j - 1):
                return False
            if i == m - 1 and j == n - 1:
                return balance == 0
            return (i + 1 < m and dfs(i + 1, j, balance)) or \
                   (j + 1 < n and dfs(i, j + 1, balance))
        return dfs(0, 0, 0)
