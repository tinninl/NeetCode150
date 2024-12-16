class Solution:
    
    def schedule(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        # Create a hashmap to map courses to its prereqs
        preMap = {c:[] for c in range(numCourses)}
        
        for c, p in prerequisites:
            preMap[c].append[p]
            
        res = []
        
        # The safe set will contain the courses that are safe to take
        # The undetermined set will contain the courses that we do not know
        # and will help us detect loops in our dfs search
        safe, undetermined = set(), set()
        
        def dfs(c):
            
            # Are we in a loop? 
            if c in undetermined:
                return False
            
            # Is this course safe to take?
            if c in safe:
                return True
            
            # Checkpoint: we do not know if the course is safe until we check its prereqs
            
            undetermined.add(c)
        
        
            for p in preMap[c]: # Check prereqs
                
                if dfs(p) == False:
                    return False
            
            # Checkpoint: We have determined that the course is safe
            
            undetermined.remove(c) # Update sets
            safe.add(c)
        
            res.append(c) # Add to result
            
            return True
    
        for c in range(numCourses):
            if not dfs(c): return []
        
        return res