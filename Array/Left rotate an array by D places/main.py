class Solution:
    def leftRotate(self, arr, d):
        n = len(arr)
        d = d % n  # in case d > n

        # helper function to reverse array in-place
        def reverse(subarr, left, right):
            while left < right:
                subarr[left], subarr[right] = subarr[right], subarr[left]
                left += 1
                right -= 1

        # Step 1: reverse first d elements
        reverse(arr, 0, d-1)
        # Step 2: reverse remaining elements
        reverse(arr, d, n-1)
        # Step 3: reverse the entire array
        reverse(arr, 0, n-1)

        return arr
