class Solution:
    def findUnion(self, a, b):
        s = set()
        union = []
    
        for num in a:
            s.add(num)   # insert all elements of arr1 into set
    
        for num in b:
            s.add(num)   # insert all elements of arr2 into set
    
        union = sorted(s)   # convert set back to list
    
        return union
        
        
