class Solution:
    def maxDepthAfterSplit(self, seq: str):
        res = []
        depth = 0
        for ch in seq:
            if ch == '(':
                depth += 1
                res.append(depth % 2)  # odd depth → group 1, even → group 0
            else:
                res.append(depth % 2)
                depth -= 1
        return res
