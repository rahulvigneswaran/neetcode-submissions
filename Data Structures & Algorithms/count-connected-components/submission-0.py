class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        res = 0
        adjList = defaultdict(list)
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
            
        def helper(node):
            
            visited.add(node)

            for nei in adjList[node]:
                if nei not in visited:
                    helper(nei)
            
        
        for i in range(n):
            if i not in visited:
                res += 1
                helper(i)
        return res