class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueOfindex : dict[int,int] = {}

        for index , n in enumerate(nums):
            diff = target - n
            if diff in valueOfindex:
                return [valueOfindex[diff],index]     
            valueOfindex[n] = index

        return []   