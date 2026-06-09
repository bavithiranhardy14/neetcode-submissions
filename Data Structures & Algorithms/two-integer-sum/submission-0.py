class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueOfIndex : List[int] = {}


        for index ,n in enumerate(nums):

            result = target - n

            if result in valueOfIndex:
                return [valueOfIndex[result],index]
            else:
                valueOfIndex[n] = index
                
        return []
        