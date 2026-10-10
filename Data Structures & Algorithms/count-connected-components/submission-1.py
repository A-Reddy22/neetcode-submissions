class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #building adjacency list
        adj_list={}
        for i in range(n):
            adj_list[i]=[]
        
        for new,old in edges:
            adj_list[new].append(old)
            adj_list[old].append(new)
        ans=0

        visited=set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in adj_list[node]:
                dfs(i)
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans+=1
        return ans