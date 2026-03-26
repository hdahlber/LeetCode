class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_val = -1
        for i in range(len(arr) - 1, -1, -1):
            place_val = right_val
            right_val = max(right_val, arr[i])
            arr[i] = place_val
            #print(arr[i])

        return arr