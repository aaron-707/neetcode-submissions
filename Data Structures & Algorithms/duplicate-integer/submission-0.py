class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        is_true = False
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])

            else:
                is_true = True
        return is_true
