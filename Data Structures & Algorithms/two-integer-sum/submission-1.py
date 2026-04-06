class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        diff = 0

        for i, j in enumerate(nums):
            diff = target - j

            if diff in result:
                return [result[diff], i]

            result[j] = i
