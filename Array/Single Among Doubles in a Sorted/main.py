class Solution:
    
        # code here
    def single(self, arr):
    # XOR all the elements:
        xorr = 0
        for num in arr:
            xorr ^= num
        return xorr
        
        
