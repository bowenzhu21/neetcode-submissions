class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for c in range(numCourses):
            adj[c] = []
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        output = []
        visit = set()
        seen = set()

        def dfs(crs):
            if crs in seen:
                return False
            if crs in visit:
                return True
            
            seen.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        

        return output