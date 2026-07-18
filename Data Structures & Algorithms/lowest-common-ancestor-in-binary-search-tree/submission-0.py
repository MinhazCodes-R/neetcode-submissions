# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p = p
        q = q
        '''
        idea is we look at p and q values
        if min (p,q) and max(p,q) are both greater than the currval
        then we reccursively go into the right branch
        if they are less than then we recurssivly go into the left branch

        if they are both less than and greater than then we return the
        node we are at

        if either is equal to the node then we reteun the node we are at
        '''

        def recursive(node):
            value = node.val

            if value < max(p.val,q.val) and value<min(p.val,q.val):
                return_node = recursive(node.right)

            elif value > max(p.val,q.val) and value>min(p.val,q.val):
                return_node = recursive(node.left)

            else:
                return node

            return return_node

        return_node = recursive(root)
        print(return_node)
        return return_node
        