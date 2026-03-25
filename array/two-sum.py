class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            if num > target:
                continue
            else:
                result = target - num
                if result in seen:
                    return [seen[result],i]
                seen[num] = i
            

        