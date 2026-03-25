class Solution:
   
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(len(nums)-1):
            left.append(left[i]*nums[i])
       

        right= 1
        for i in range(len(nums)-1,-1,-1):
            left[i] = left[i] * right
            right = right* nums[i]


        #print(left)
        return left