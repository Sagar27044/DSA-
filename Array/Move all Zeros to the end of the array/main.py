
class Solution:
    def pushZerosToEnd(self, arr):
        j = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]  # swap
                j += 1
        return arr
