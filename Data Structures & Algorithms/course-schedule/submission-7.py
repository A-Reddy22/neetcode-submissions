class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursmap={}
        for i in range(numCourses):
            coursmap[i]=[]
        courses=prerequisites
        
        for pre,course in courses:
            coursmap[pre].append(course)
        # now we have to check if there are cycles
        visiting=set()

        def dfs(course):
            if coursmap[course]==[]:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for i in coursmap[course]:
                
                if not dfs(i):
                    return False
            visiting.remove(course)
            coursmap[course]=[]
            return True

            
            


        #this is the end code where we call dfs
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        