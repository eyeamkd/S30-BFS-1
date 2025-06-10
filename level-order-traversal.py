'''
Time Complexity: O(n)
Space Complexity: O(n) since we store all nodes in the queue. 

Approach: 
1. Use a queue to perform a level order traversal of the binary tree.
2. For each node in the queue, append its value to the output list.
3. Pop the first node from the queue and append its left and right children to the queue.
4. Repeat step 3 until the queue is empty.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        output = []
        if root:
            queue.append(root)

        while len(queue)>0:
            level_size = len(queue)
            level = []
            while level_size>0:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
                level_size-=1 
            output.append(level)

        return output
            

'''
Approach using the DFS with HashMap
Time Complexity: O(n)
Space Complexity: O(n) since we store all nodes in the output dictionary with Bucket sorting.
'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        output = defaultdict(list)

        def dfs(node, depth):
            if not node:
                return

            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

            output[depth].append(node.val)

        dfs(root, 0)

        print(output)
        res = []

        i = 0 

        while len(output[i])>0:
            res.append(output[i])
            i+=1
        
        return res

'''
Approach using the DFS with List 
Time Complexity: O(n)
Space Complexity: O(n) since we store all nodes in the output list.
'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        output = []

        def dfs(node, depth):
            if not node:
                return
            if len(output) == depth:
                output.append([])

            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

            output[depth].append(node.val)

        dfs(root, 0)

        return output
