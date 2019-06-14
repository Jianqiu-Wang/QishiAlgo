#Runtime: 40 ms, faster than 51.50% of Python3 online submissions for Search in Rotated Sorted Array.
#Memory Usage: 13.3 MB, less than 30.72% of Python3 online submissions for Search in Rotated Sorted Array.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        if len(nums) == 1: 
            if nums[0] == target: return 0
            else: return -1
 
        if nums[0] < nums[-1]: # no rotation 
            return self.binary_search(nums, target)
        else:
            start = 0
            end = len(nums) - 1
            while start < end - 1:
                mid = (start + end) // 2
                if nums[mid] > nums[-1]:
                    start = mid
                else:
                    end = mid

            if nums[start] < nums[end]: 
                min_idx = start
                min_value = nums[start]
            else:
                min_idx = end
                min_value = nums[end]
            nums = nums[min_idx:] + nums[:min_idx]
            print(nums)
            res = self.binary_search(nums, target)
            print("result ", res)
            if res >= 0:
                idx = res + min_idx 
                print("idx", idx)
                if idx > len(nums) - 1:
                    return idx - len(nums)
                else:
                    return idx
            return -1
            
    def binary_search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start < end -1:
            mid = (start + end ) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums) - 1
        return -1
