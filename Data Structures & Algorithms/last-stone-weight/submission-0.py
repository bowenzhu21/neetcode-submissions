class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for n in stones:
            heap.append(-n)
        heapq.heapify(heap)
        

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x < y:
                heapq.heappush(heap, -(y-x))
        
        if heap:
            return -heap[0]
        return 0