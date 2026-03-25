class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for i in range(len(nums)):
            length = len(myset)
            myset.add(nums[i])
            if length == len(myset):
                return True
        return False 
        