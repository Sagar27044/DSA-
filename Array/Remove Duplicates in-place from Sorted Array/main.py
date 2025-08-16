class Solution:
    def removeDuplicates(self, arr):
        # code here 
        if not arr:  
            return []
    
        result = [arr[0]]  # first element is always unique
    
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:  # check if different from previous
                result.append(arr[i])
    
        return result
