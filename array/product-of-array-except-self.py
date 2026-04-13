import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        F = [nums[0:i] + nums[i+1:] for i in range(len(nums))]
        print(F)
        result = []
        for x in range(len(nums)):
            nums[x] = math.prod(F[x])
            print(nums)
        return nums