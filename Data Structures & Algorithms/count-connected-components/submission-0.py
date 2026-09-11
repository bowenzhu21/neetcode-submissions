class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()

        def dfs(node):
            seen.add(node)

            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)

        components = 0

        for node in range(n):
            if node not in seen:
                dfs(node)
                components += 1

        return components