# -*- coding:utf-8 -*-

'''
c
## 31.二叉搜索树与双向链表

**输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。**

不会
不会
不会
思路：
下面的代码也看的不是很懂



'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return None

        def find_right(node):
            while node.right:
                node = node.right
            return node

        leftNode = self.Convert(pRootOfTree.left)
        rightNode = self.Convert(pRootOfTree.right)

        retNode = leftNode

        if leftNode:
            leftNode = find_right(leftNode)
        else:
            retNode = pRootOfTree

        pRootOfTree.left = leftNode
        pRootOfTree.right = rightNode

        if leftNode != None:
            leftNode.right = pRootOfTree
        if rightNode != None:
            rightNode.left = pRootOfTree

        return retNode



'''


         5
       /  \	
      2    9
     /\    /\
    1 3   6 11

'''

root = TreeNode(5)

root1 =  TreeNode(1)
root3 = TreeNode(3)

root2 =  TreeNode(2)
root2.left = root1
root2.right = root3

root.left = root2

# ==========

root11 =  TreeNode(11)
root6 = TreeNode(6)

root9 =  TreeNode(9)
root9.right = root11
root9.left  = root6
root.right = root9

a = Solution()
a.Convert(root)
