class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #first i create an adjacency list 
        adj_list={}
        courses=prerequisites
        for i in range(numCourses):
            adj_list[i]=[]
        for course,prereq in courses:
            adj_list[course].append(prereq)

        visited=set()
        ans=[]
        completed=set()

        def dfs(course):
            if course in completed:
                return True
            if course in visited:
                return False
            visited.add(course)
            for i in adj_list[course]:
                if not dfs(i):
                    return False
            adj_list[course]=[]
            visited.remove(course)
            completed.add(course)
           
            ans.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans
                
                
            

        
        
        
        