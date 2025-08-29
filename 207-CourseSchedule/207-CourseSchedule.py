# Last updated: 8/29/2025, 6:25:31 AM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 <= a_i, b_i < numCourses
        precourse = {i:[] for i in range(numCourses)}
        visited = set()

        for course, prereq in prerequisites:
            precourse[course].append(prereq)
        
        def dfs(course):
            if course in visited: # Cycle
                return False
            # We'll be popping from the prereq array of each course, so the base case is
            # when our course has an empty array
            if precourse[course] == []:
                return True
            
            visited.add(course)

            # Traverse through each element in the pre req
            for prereq in precourse[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            precourse[course] = []
            return True
        for courses in range(numCourses):
            if not dfs(courses):
                return False
        return True
