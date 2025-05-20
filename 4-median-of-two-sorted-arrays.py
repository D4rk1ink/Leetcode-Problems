class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = []
        i, j = 0
        while len(nums1) < i and len(nums) < j:
            if nums[i] < nums[j]:
                merged.append(nums[i])
                i = i + 1
            else:
                merged.append(nums[j])
                j = j + 1
        print(merged)