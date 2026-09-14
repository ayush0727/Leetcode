class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (rec1[2] <= rec2[0] or
                    rec2[2] <= rec1[0] or
                    rec1[3] <= rec2[1] or
                    rec2[3] <= rec1[1])
if __name__ == "__main__":
    s = Solution()
    print(s.isRectangleOverlap([0,0,2,2], [1,1,3,3]))  # True
    print(s.isRectangleOverlap([0,0,1,1], [1,0,2,1]))  # False
    print(s.isRectangleOverlap([0,0,1,1], [2,2,3,3]))  # False
