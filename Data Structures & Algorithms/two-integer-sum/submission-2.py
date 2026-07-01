class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        for i, val1 in enumerate(nums):
            for j in range(i+1, len(nums)):
                if val1 + nums[j] == target:
                    return [i, j]


        