class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        fact = [1] * (n + k + 1)
        inv_fact = [1] * (n + k + 1)
        
        for i in range(1, n + k + 1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact[n+k] = pow(fact[n+k], MOD-2, MOD)
        for i in range(n+k, 0, -1):
            inv_fact[i-1] = inv_fact[i] * i % MOD
        
        def nCr(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a-b] % MOD
        
        return nCr(n+k-1, 2*k)
