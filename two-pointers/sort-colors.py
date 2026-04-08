class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #is either 0, 1, or 2.
        zeroes = 0
        ones = 0
        twos = 0
        for num in nums:
            if num == 0:
                zeroes += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1

        for i in range(len(nums)):
            if i < zeroes:
                nums[i] = 0
            elif i < zeroes + ones:
                nums[i] = 1
            else:
                nums[i] = 2

        