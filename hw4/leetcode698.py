# 1948ms
"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:
1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 0: return True
        array_sum = sum(nums)
        array_len = len(nums)
        if array_sum % k: return False
        group_sum = array_sum / k
        nums = sorted(nums)
        if nums[-1] > group_sum: return False
        crtsum_list = [0] * k
        nums = nums[::-1] # reorder from large to small element
        def dfs(idx, crtsum_list):
            if idx == array_len: return True # looped over all integers
            for i, crtsum in enumerate(crtsum_list):
                if nums[idx] + crtsum <= group_sum:    
                    crtsum_list[i] += nums[idx]
                    if dfs(idx+1, crtsum_list): 
                        return True
                    else:
                        crtsum_list[i] -= nums[idx] 
            return False
        
        return dfs(0, crtsum_list)
        