'''
Time Complexity: O(n+p) where n is the number of courses and p is the number of prerequisites.
Space Complexity: O(n) since we store all nodes in the queue.

Approach: 
1. Build a graph from the input.
2. Use BFS to find all the nodes that have in-degree 0.
3. Return true if the number of nodes in the graph is 0.
4. Return false otherwise.  
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build the graph 

        graph = defaultdict(list)
        in_degree = [0]*numCourses

        for node in prerequisites:
            second, first = node
            graph[first].append(second)
            in_degree[second]+=1
        
        queue = deque()

        for course in range(len(in_degree)):
            if in_degree[course]==0:
                queue.append(course)
            
        while queue:
            course = queue.popleft()
            numCourses-=1 

            for neighbor in graph[course]:
                in_degree[neighbor]-=1 
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
        
        return numCourses==0



