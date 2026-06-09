class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        duplicate : bool = False
        seen = {}

        for n in nums:
            if n in seen:
                duplicate = True
                seen[n] += 1
                return duplicate
            else:
                seen[n] = 1
        return False