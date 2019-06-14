#Runtime: 32 ms, faster than 98.89% of Python3 online submissions for Sqrt(x).
#Memory Usage: 13.3 MB, less than 41.95% of Python3 online submissions for Sqrt(x).
class Solution:
    def mySqrt(self, x: int) -> int:
        """ find y satisfying y^2 <= x and (y+1)^2 >x using binary search
        """
        start = 0
        end = x
        while start < end - 1:
            mid = start + (end - start) // 2 
            if mid * mid > x:
                end = mid
            else:
                start = mid
        if x == 1: return 1
        return start
