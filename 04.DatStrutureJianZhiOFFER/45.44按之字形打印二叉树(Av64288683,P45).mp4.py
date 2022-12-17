# -*- coding:utf-8 -*-
# 45.44按之字形打印二叉树(Av64288683,P45).mp4


'''
题目描述

思路：
有堆栈解决，先进后出，后进先出


'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# 返回二维列表[[1,2],[4,5]]
	def Print(self, pRoot):
		if pRoot == None:
			return []
		stack1 = [pRoot]
		stack2 = []
		retList = []
		while stack1 or stack2:
			tmpList = []
			while stack1:
				# tmp = queue1[0]
				# del queue1[0]
				tmp = stack1.pop()
				tmpList.append(tmp.val)
				if tmp.left:
					stack2.append(tmp.left)
				if tmp.right:
					stack2.append(tmp.right)

			if tmpList:
				retList.append(tmpList)

			tmpList = []
			while stack2:
				# tmp = queue2[-1]
				tmp = stack2.pop()
				tmpList.append(tmp.val)
				if tmp.right:
					stack1.append(tmp.right)
				if tmp.left:
					stack1.append(tmp.left)
			if tmpList:
				retList.append(tmpList)
		return retList

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
print(  a.Print(root) )		# [[5], [9, 2], [1, 3, 6, 11]]
