class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = arr[-1]          # greatest element to the right of last index is -1, but we'll set last later
        for i in range(len(arr)-2, -1, -1):
            temp = arr[i]           # save original value
            arr[i] = rightMax       # replace with current greatest to the right
            rightMax = max(rightMax, temp)   # update greatest for next iteration
        arr[-1] = -1                # last element always becomes -1
        return arr