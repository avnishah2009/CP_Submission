class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        numbers = dict()
        count = 0
        n = len(A)

        for num in A:
            numbers[num] = 1

        for num in range(n):
            if (A[num] - 1) not in numbers:
                curr_val = A[num]
                while (curr_val in numbers):
                    curr_val += 1

                if curr_val - A[num] > count:
                    count = curr_val - A[num]

        return count
#print longestConsecutive([1, 9, 3, 10, 4, 20, 2, 12,13,14,15,16,17])
