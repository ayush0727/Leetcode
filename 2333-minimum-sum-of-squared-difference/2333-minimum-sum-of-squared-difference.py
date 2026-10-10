class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int],
                         k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        if sum(diff) <= k:
            return 0
        left, right = 0, max(diff)
        while left < right:
            mid = (left + right) // 2
            ops = 0
            for d in diff:
                if d > mid:
                    ops += d - mid
            if ops > k:
                left = mid + 1
            else:
                right = mid
        t = left
        arr = []
        used = 0
        for d in diff:
            if d > t:
                used += d - t
                arr.append(t)
            else:
                arr.append(d)

        remain = k - used

        arr.sort(reverse=True)
        i = 0
        while remain > 0:
            if arr[i] > 0:
                arr[i] -= 1
                remain -= 1
            i += 1
        return sum(x * x for x in arr) 