class Solution:
    def maxConsecBits(self, arr: list[int]) -> int:
        cnt = 1        # at least 1 element exists (arr size ≥ 1)
        maxi = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                cnt += 1
            else:
                cnt = 1
            maxi = max(maxi, cnt)

        return maxi
