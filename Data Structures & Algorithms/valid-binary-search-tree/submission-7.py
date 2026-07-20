# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node,min_val,max_val):
            if node==None: return True

            if node.val<=min_val or node.val>=max_val:

                return False

            #dfs left
            left_dfs = dfs(node.left,min_val,node.val)

            #dfs right
            right_dfs = dfs(node.right,node.val,max_val)


            if not left_dfs or not right_dfs: return False

            return True


        min_val,max_val = -float('inf'),float('inf')
        return dfs(root,min_val,max_val)






