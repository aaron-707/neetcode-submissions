from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    

        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        x = sorted(count, key=count.get, reverse = True)
        return x[:k]