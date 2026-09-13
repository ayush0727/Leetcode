class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        shift_count = {}        
        for (x1, y1) in ones1:
            for (x2, y2) in ones2:
                dx, dy = x2 - x1, y2 - y1
                shift_count[(dx, dy)] = shift_count.get((dx, dy), 0) + 1       
        return max(shift_count.values() or [0])