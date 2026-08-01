class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for i, j in prerequisites:
            adjList[i].append(j)
        
        visited = set()

        def helper(node):            
            if node in visited:
                return False
            
            visited.add(node)

            for nei in adjList[node]:
                if not(helper(nei)):
                    return False
            adjList[node] = []
            visited.remove(node)

            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not helper(i):
                    return False

        return True

        # O(V + E), O(V + E)
        



