#Submitted-1, 860ms

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            num_2 = target - num
            try:
                j = nums.index(num_2)
                if i != j:
                    return [i, j]
            except:
                pass