def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
    
    preMap = { i:[] for i in range(numCourses)}
    
    for c, p in prerequisites:
        preMap[c].append(p)
        
    visit = set()
    
    def dfs(c):
        
        # if we already checked this course, we are in a loop 
        if c in visit:
            return False

        # no prequisites? can take
        if preMap(c) == []:
            return True
        
        visit.add(c)
        
        # Check prereqs to determine if this course can be taken
        for p in preMap[c]:
            
            if not dfs(p):
                return False
        
        # This course can be taken, so it is ok to check this course again
        # Therefore, remove from set and empty its prereqs list
        visit.remove(c)
        preMap[c] = []
        
        return True
    
    # Check every course
    for c in range(numCourses):
        
        if not dfs(c): 
            return False
        
    return True