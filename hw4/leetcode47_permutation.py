"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution:
    def permuteUnique(self, nums):
        if not nums: return []
        nums = sorted(nums)
        res = []
        visited = [False] * len(nums)
        
        def backtrack(perm):
            if len(nums) == len(perm):
                res.append(perm)
                print(perm)
                # print("res", res)
            for i in range(len(nums)):
                if visited[i] or (i>0 and nums[i]==nums[i-1] and not visited[i-1]):
                    continue
                visited[i] = True
                # print(perm)
                # print("index i",i)
                # print("nums i ",nums[i])
                perm.append(nums[i])
                backtrack(perm)
                perm.pop(nums[i])
                visited[i] = False
        
        backtrack(res)
        return res

if __name__ == "__main__":
    nums = [1,1,2]

    print(Solution().permuteUnique(nums))
    #[1, 1, 6], [1, 2, 5], [1, 7], [1, 2, 5], [1, 7], [2, 6]]