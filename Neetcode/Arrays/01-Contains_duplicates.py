from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        # Iterate through the list
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False