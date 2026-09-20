class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i, ch in enumerate(s, start=1):
            # 'a' should map to 26, 'z' to 1
            reversed_index = 26 - (ord(ch) - ord('a'))
            total += reversed_index * i
        return total

sol = Solution()
print(sol.reverseDegree("abc"))   # Output: 148
print(sol.reverseDegree("zaza"))  # Output: 160

        