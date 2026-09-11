class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        moves = ((1,0), (-1,0), (0,1), (0,-1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist

                for dr, dc in moves:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and (r, c) not in visit and grid[r][c] == 2147483647:
                        q.append((r, c))
                        visit.add((r, c))
                
            dist += 1