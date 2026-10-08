class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list={}
        #creating a matrix that maps a course to its prereqs
        courses=prerequisites
        for i in range(numCourses):
            adj_list[i]=[]
        for course,pre in courses:
            adj_list[(course)].append(pre)
        
        visited=set()
        def dfs(course):
            if course in visited:
                return False
            if adj_list[course]==[]:
                return True
            visited.add(course)
            # need to loop through prereqs of course which is adj_list[course]
            for i in adj_list[course]:
                if not dfs(i):
                    return False
            visited.remove(course)
            adj_list[course]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            