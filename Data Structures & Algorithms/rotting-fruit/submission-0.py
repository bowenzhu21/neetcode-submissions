class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
        q = deque()
        seen = set()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    seen.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        time = 0
        while q and fresh > 0:
            length = len(q)
            for _ in range(length):
                row, col = q.popleft()
                for dr, dc in moves:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in seen:
                        seen.add((r, c))
                        q.append((r, c))
                        fresh -= 1
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1




