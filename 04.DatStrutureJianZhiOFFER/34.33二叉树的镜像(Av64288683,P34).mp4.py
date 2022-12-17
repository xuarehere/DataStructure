# -*- coding:utf-8 -*-
'''
34.33二叉树的镜像(Av64288683,P34).mp4

**操作给定的二叉树，将其变换为源二叉树的镜像。**

##### `输入描述:`
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5


不会
不会
不会


思路：采用先序遍历进行交换就可以了，比较简单
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	# 返回镜像树的根节点
	def Mirror(self, root):
		# write code here
		if not root:
			return None

		def preOrder(inRoot):
			if not inRoot:
				return None
			# inRoot.val
			if inRoot.left or inRoot.right:
				inRoot.left, inRoot.right = inRoot.right, inRoot.left
			preOrder(inRoot.left)
			preOrder(inRoot.right)
			return inRoot

		return preOrder(root)