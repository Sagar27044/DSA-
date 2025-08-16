class Solution:
    def missingNum(self, a):
        # code here
        N=len(a)+1
    # N is the expected largest number in the sequence
        summation = (N * (N + 1)) // 2
        s2 = sum(a)
        missingNum = summation - s2
        return missingNum
