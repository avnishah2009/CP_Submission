import heapq


def kthsmallest(A, B):
    heap = []
    for number in A:
        heapq.heappush(heap, number)

    for i in range(B):
        number = heapq.heappop(heap)

    return number

print kthsmallest([2,1,3,4,], 3)
