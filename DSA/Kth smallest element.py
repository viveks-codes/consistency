import heapq

def kthSmallest(arr,k):
        heapq.heapify(arr)
        i = 0
        while i+1 < k:
            heapq.heappop(arr)
            i += 1
        return heapq.heappop(arr)
print(kthSmallest([5,10,58,8,4,1,2,5,74,5], k=4))