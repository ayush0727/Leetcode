class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        closestX = min(max(xCenter, x1), x2)
        closestY = min(max(yCenter, y1), y2)
        dx = closestX - xCenter
        dy = closestY - yCenter

        return dx * dx + dy * dy <= radius * radius

if __name__ == "__main__":
    s = Solution()
    print(s.checkOverlap(1, 0, 0, 1, -1, 3, 1))   # True
    print(s.checkOverlap(1, 1, 1, 1, -3, 2, -1))  # False
    print(s.checkOverlap(1, 0, 0, -1, 0, 0, 1))   # True
