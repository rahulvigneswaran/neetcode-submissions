class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        adjList = defaultdict(list)

        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        def helper(node, prev):
            if node in visited:
                return False

            visited.add(node)

            for nei in adjList[node]:
                if nei == prev:
                    continue
                if not(helper(nei, node)):
                    return False
            return True

        return helper(0, -1) and len(visited) == n 

        # O(V + E), O(V + E)
