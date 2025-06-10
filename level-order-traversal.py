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
            