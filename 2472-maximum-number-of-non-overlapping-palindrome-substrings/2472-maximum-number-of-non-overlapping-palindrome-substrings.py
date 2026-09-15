class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        pals = [[] for _ in range(n)]       
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    pals[l].append(r)
                l -= 1
                r += 1        
        for i in range(n):
            expand(i, i)       
            expand(i, i + 1)          
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] 
            for r in pals[i]:
                dp[i] = max(dp[i], 1 + dp[r + 1])
        
        return dp[0]
sol = Solution()
print(sol.maxPalindromes("abaccdbbd", 3))  
print(sol.maxPalindromes("adbcda", 2))     
