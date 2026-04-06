class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0 
        left = 0
        max_len = 0


        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_len = max(max_len, count[s[right]])

            while (right - left + 1) - max_len > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res
        