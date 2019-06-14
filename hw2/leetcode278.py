#Runtime: 32 ms, faster than 94.77% of Python3 online submissions for First Bad Version.
#Memory Usage: 13.1 MB, less than 69.45% of Python3 online submissions for First Bad Version.

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1): return 1
        if n == 1: return 1
        # if n <= 2: 
            # if isBadVersion(1): return 1
            # else: return 2
        start = 1
        end = n
        while start < end :    
            mid = start + (end - start) // 2
            print(start, end, mid)
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start
