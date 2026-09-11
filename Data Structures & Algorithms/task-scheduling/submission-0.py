class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        tasks = Counter(tasks)
        heap = []
        for cnt in tasks.values():
            heap.append(-cnt)
        
        heapq.heapify(heap)
        time = 0
        while heap or queue:
            time += 1
            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1
                if cnt != 0:
                    queue.append((time + n, cnt))

            if queue and queue[0][0] == time:
                _, cnt2 = queue.popleft()
                heapq.heappush(heap, cnt2)
        
        return time

