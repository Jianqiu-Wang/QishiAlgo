class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums_sum = []
        for i in range(len(nums)):
            if not nums_sum:      # add first element 
                nums_sum.append(nums[i])
            elif nums_sum[-1] < 0: # drop last sum if it less than 0
                nums_sum.append(nums[i])
            else: # update last sum by adding crt num
                nums_sum.append(nums_sum[-1] + nums[i])
        if not nums_sum: return max(nums)
        return max(nums_sum)