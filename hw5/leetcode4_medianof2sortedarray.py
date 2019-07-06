class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        m = len(nums1)
        n = len(nums2)
        nums = []
        i = 0
        j = 0

        if m==0 or n==0:
            nums = nums1 + nums2
            if (m+n) % 2:
                return nums[int((m+n)/2)]
            else:
                return (nums[int((m+n)/2)-1] + nums[int((m+n)/2)]) /2
        
        while len(nums) < m + n:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                if i < m - 1:
                    i = i + 1
                else:
                    nums = nums + nums2[j:]
                    break
            else:
                nums.append(nums2[j])
                if j < n - 1:
                    j = j + 1
                else:
                    nums = nums + nums1[i:]
                    break
        
        if (m+n) % 2:
            return nums[int((m+n)/2)]
        else:
            return (nums[int((m+n)/2)-1] + nums[int((m+n)/2)]) /2.