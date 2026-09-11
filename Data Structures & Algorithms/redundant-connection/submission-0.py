class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]  # Path compression
                node = parent[node]

            return node

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            # Attach the smaller tree to the larger tree
            if rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
                rank[root_b] += rank[root_a]
            else:
                parent[root_b] = root_a
                rank[root_a] += rank[root_b]

            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]