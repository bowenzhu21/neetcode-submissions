class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        seen = set()
        self.largest = 0

        def bfs(r, c):
            q = collections.deque()
            seen.add((r, c))
            q.append((r, c))
            size = 1
            while q:
                row, col = q.popleft()
                moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
                for dr, dc in moves:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in seen:
                        q.append((r, c))
                        seen.add((r, c))
                        size += 1
            
            self.largest = max(self.largest, size)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    bfs(r, c)
        
        return self.largest