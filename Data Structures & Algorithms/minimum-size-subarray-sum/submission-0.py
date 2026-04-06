class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        count = 0
        res = float("inf")

        for right in range(len(nums)):
            count += nums[right]

            while count >= target:
                res = min(res, right - left + 1)
                count -= nums[left]
                left += 1

        return 0 if res == float("inf") else res 
        