class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = []
        for n,i in cnt.items():
            heap.append([-i,n])
        heapq.heapify(heap)

        res = []
        for j in range(k):
            _, n = heapq.heappop(heap)
            res.append(n)
        
        return res