class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #first we build an adjacecy list
        #then we have a visited set
        #keep a prev node so we know if that is hwat we previously visited 
        #first vreate an adjacency matrix
        adj_list={}
        for i in range(n):
            adj_list[i]=[]
        
        for first,last in edges:
            adj_list[first].append(last)
            adj_list[last].append(first)
        
        visited=set()
        def dfs(edge,prev):
            if edge in visited:
                return False
            visited.add(edge)
            for nei in adj_list[edge]:
                
                if nei==prev:
                    continue
                if not dfs(nei,edge):
                    return False
            return True
        return dfs(0,-1) and len(visited)==n
            
        
        