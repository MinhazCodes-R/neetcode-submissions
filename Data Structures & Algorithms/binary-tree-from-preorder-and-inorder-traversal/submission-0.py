# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #partition the list

        '''
        [1,2,3,3,5,6]
        '''

        preorder_index = 0

        def create_tree(inorder:List[int]):
            nonlocal preorder_index

            if not inorder: return
            
            our_val = preorder[preorder_index]
            our_node = TreeNode(preorder[preorder_index])
            preorder_index += 1


            inorder_index = inorder.index(our_val)
            left_list = inorder[:inorder_index]
            right_list = inorder[inorder_index+1:]

            '''
            the idea is that set node
            curr node is preorder[o]
            '''

            our_node.left = create_tree(left_list)
            our_node.right = create_tree(right_list)

            return our_node

        return_node = create_tree(inorder)
        return return_node
        