# Last updated: 8/29/2025, 12:40:33 AM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i :[] for i in range(numCourses)}
        visited = set()

        for course, prereq in prerequisites:
            premap[course].append(prereq)
        
        # perform cycle detection using dfs
        # If the pre requisite course is a course we have to take, then it's doom
        def dfs(course):
            if course in visited:
                return False
            
            if premap[course] == []:
                return True
            
            visited.add(course)

            for pre in premap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            premap[course] = []
            return True
        for courses in range(numCourses):
            if not dfs(courses):
                return False
        return True