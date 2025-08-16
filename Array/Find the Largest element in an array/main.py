class Solution:
    def largest(self, arr):
        n=len(arr)
        # code here
        max=arr[0]
        for i in range(0,n):
            if max<arr[i]:
                max=arr[i]
        return max
            
        
