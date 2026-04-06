class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = {}

        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1

        sorted_result = sorted(result, key=lambda x: result[x])
        return sorted_result[-k:]





        