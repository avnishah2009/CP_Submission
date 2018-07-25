import heapq

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer

    def kthsmallest(self, A, B):
        heap = []
        for number in A:
            heapq.heappush(heap, number)
    
        for i in range(B):
            number = heapq.heappop(heap)
    
        return number
    
    #rint kthsmallest([2,1,3,4,], 3)
