class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:  # Check if it's consecutive
                current_streak += 1
            elif nums[i] != nums[i - 1]:  # Ignore duplicates
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1  # Reset the streak

        return max(longest_streak, current_streak)
