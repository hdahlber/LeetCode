class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        winner = -1
        amount = 0

        for x in nums:
            if amount == 0:
                winner = x      
                amount = 1
            else:
                if x == winner: 
                    amount += 1
                else:
                    amount -= 1
                    
        return winner