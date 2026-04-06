class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_s = re.sub(r'[^a-z0-9]', '', s.lower())
        return normalized_s == normalized_s[::-1]


        