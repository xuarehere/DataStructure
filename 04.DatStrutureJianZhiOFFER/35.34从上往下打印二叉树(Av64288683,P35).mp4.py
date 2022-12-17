# -*- coding:utf-8 -*-
'''
35.34从上往下打印二叉树(Av64288683,P35).mp4

## 28.从上往下打印二叉树

**从上往下打印出二叉树的每个节点，同层节点从左至右打印。**

思路：
	层次遍历法。
	使用队列
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	# 返回从上到下每个节点值列表，例：[1,2,3]
	def PrintFromTopToBottom(self, root):
		# write code here
		if not root:
			return []

		queue = [root]
		ret = []
		while queue:
			tmp = queue.pop(0)
			ret.append(tmp.val)
			if tmp.left:
				queue.append(tmp.left)
			if tmp.right:
				queue.append(tmp.right)
		return ret

