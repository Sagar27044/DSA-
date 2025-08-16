class Solution:
    def rotate(self, arr):
        n = len(arr)
        if n == 0:  # handle empty array
            return
        temp = arr[-1]  # store the last element
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]  # shift elements to the right
        arr[0] = temp  # place last element at the start
