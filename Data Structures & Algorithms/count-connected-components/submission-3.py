class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list={}
        for i in range(n):
            adj_list[i]=[]
        for start,end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)
        visited=set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in (adj_list[node]):
                dfs(i)
        ans=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans+=1
        return ans
        