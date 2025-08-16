Find the Largest Element in an Array

Problem Statement:
Given an array of numbers, find the largest element in the array.

Example:

Input: [3, 5, 7, 2, 8]
Output: 8


Edge Cases to Consider:

Array with all negative numbers

Array with only one element

Array with all elements the same

Empty array

Approach / Explanation:

Initialize a variable largest with the first element of the array.

Traverse the array from the second element onward.

For each element, compare it with largest.

If the element is greater, update largest.

After checking all elements, largest contains the maximum value.

Time Complexity: O(n) → Traverses the array once
Space Complexity: O(1) → Uses a single extra variable
