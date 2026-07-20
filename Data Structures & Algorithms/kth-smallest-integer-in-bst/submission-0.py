# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        k_arr = []

        def dfs(node):
            nonlocal k_arr

            #base cases
            if node == None: return
            if len(k_arr)>=k: return

            dfs(node.left)
            k_arr.append(node.val)
            dfs(node.right)

            return

        dfs(root)
        return k_arr[k-1]
        