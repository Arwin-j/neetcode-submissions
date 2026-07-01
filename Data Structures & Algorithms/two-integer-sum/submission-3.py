class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        sums = {}

        for i, val in enumerate(nums):
            compliment = target - val
            if compliment not in sums:
                sums[val] = i
            else:
                return [sums[compliment], i]



        