class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}       
        for ch in s:
            if ch in mapping:  # closing bracket
                top = stack.pop() if stack else '#'
                if mapping[ch] != top:
                    return False
            else:  # opening bracket
                stack.append(ch)        
        return not stack
   