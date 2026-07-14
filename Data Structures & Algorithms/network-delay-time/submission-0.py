class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mapping = {}
        for start_node, point_node, time in times:
            mapping.setdefault(start_node, []).append((point_node, time))

        min_heap = [(0, k)]          # (time, node)  <-- order matters
        visited = set()
        max_time = 0

        while min_heap:
            time_to_node, next_node = heapq.heappop(min_heap)

            if next_node in visited:
                continue

            visited.add(next_node)
            max_time = time_to_node   # pops are non-decreasing, so this is the running max

            for neighbour, time in mapping.get(next_node, []):
                if neighbour not in visited:
                    heapq.heappush(min_heap, (time_to_node + time, neighbour))

        return max_time if len(visited) == n else -1