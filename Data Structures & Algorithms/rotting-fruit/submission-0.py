class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        seen, need_seen = set(), set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: continue
                need_seen.add((r, c))
                if grid[r][c] == 2: queue.append((0, r, c))

        time = 0
        while queue:
            t, r, c = queue.popleft()
            if (r, c) in seen: continue
            seen.add((r, c))
            time = max(time, t)
            for nr, nc in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in seen:
                    queue.append((t+1, nr, nc))

        return time if seen == need_seen else -1