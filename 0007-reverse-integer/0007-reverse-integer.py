class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1       
        sign = -1 if x < 0 else 1
        x *= sign  # only with positive       
        result = 0
        while x != 0:
            digit = x % 10
            x //= 10                       
            if result > (INT_MAX - digit) // 10:
                return 0            
            result = result * 10 + digit        
        return sign * result
