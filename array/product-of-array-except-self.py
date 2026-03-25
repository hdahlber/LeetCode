import functools

class Solution:
   
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        @cache
        def helper(index: int) -> int:
            result = 1
            for i in range(n):
                if i != index:
                    result *= nums[i]
            return result
        
        return [helper(i) for i in range(n)]
            