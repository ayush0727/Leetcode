class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
        intervals = []
        for ch in first:
            l, r = first[ch], last[ch]
            i = l
            while i <= r:
                if first[s[i]] < l:
                    l = first[s[i]]
                    i = l
                r = max(r, last[s[i]])
                i += 1
            intervals.append((l, r))
        intervals.sort(key=lambda x: x[1])  
        res = []
        prev_end = -1
        for l, r in intervals:
            if l > prev_end:
                res.append(s[l:r+1])
                prev_end = r
        return res
