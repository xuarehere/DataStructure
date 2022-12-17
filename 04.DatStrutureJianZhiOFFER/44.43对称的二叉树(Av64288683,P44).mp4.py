# -*- coding:utf-8 -*-



# 44.43对称的二叉树(Av64288683,P44).mp4
'''
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。


'''

'''


用例:
{8,6,9,5,7,7,5}

对应输出应该为:

false


用例:
{8,6,6,5,7,7,5}

对应输出应该为:

true


'''

'''
# 我的解答：
# 错在那儿？？

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	def isSymmetrical(self, pRoot):
		# write code here

		queue1 = [pRoot]
		queue2 = []
		ret = []
		while queue1 or queue2:
			if queue1:
				tmpList = []
				while queue1:
					tmpNode = queue1[0]
					del queue1[0]
					tmpList.append(tmpNode.val)
					if tmpNode.left and tmpNode.right:
						queue2.append(tmpNode.left)
						queue2.append(tmpNode.rght)
					elif tmpNode.left or tmpNode.right:
						return False
					# 
				
					# if tmpNode.left:
					# 	queue2.append(tmpNode.left)
					# if tmpNode.right:
					# 	queue2.append(tmpNode.rght)
				if tmpList[0].val == tmpList[-1].val:
					del tmpList[0]
					del tmpList[-1]
				elif tmpList == []:
					pass
				else:
					return False
			# ret.append(tmpList)

			if queue2:
				tmpList = []
				while queue2:
					tmpNode = queue2[0]
					del queue2[0]
					tmpList.append(tmpNode.val)
					if tmpNode.left and tmpNode.right:
						queue2.append(tmpNode.left)
						queue2.append(tmpNode.rght)
					elif tmpNode.left or tmpNode.right:
						return False
					
					# 
					# if tmpNode.left:
					# 	queue1.append(tmpNode.left)
					# if tmpNode.right:
					# 	queue1.append(tmpNode.rght)
					
				if tmpList[0].val == tmpList[-1].val:
					del tmpList[0]
					del tmpList[-1]
				elif tmpList == []:
					pass
				else:
					return False
					
			# ret.append(tmpList)
			return True

'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	def isSymmetrical(self, pRoot):
		# write code here
		if pRoot == None:
			return True

		def judgeSym(left, right):
			if left == None and right == None:
				return True
			elif left == None or right == None:
				return False
			if left.val == right.val:
				retLeft = judgeSym(left.left, right.right)
				retRight = judgeSym(left.right, right.left)
				return retLeft and retRight
			else:
				return False

		return judgeSym(pRoot.left, pRoot.right)



'''
下面解法错误

'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	def isSymmetrical(self, pRoot):
		# write code here
		if not pRoot:
			return False
		queue = [pRoot]
		while queue:
			tmpNodeL = queue.pop(0)
			if queue:
				tmpNodeR = queue.pop(-1)
				if tmpNodeL.val != tmpNodeR.val:
					return False
			if tmpNodeL.left:
				queue.append(tmpNodeL.left)

			if tmpNodeL.right:
				queue.append(tmpNodeL.right)
		return True


'''
下面解法错误

'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	def isSymmetrical(self, pRoot):
		# write code here
		if not pRoot:
			return False
		queue = [pRoot]
		index = -1
		while queue:
			tmpNodeL = queue.pop(0)
			if queue:
				if tmpNodeL.val != queue[index].val:
					return False
				index -= 1
			else:
				index = -1

			if tmpNodeL.left:
				queue.append(tmpNodeL.left)

			if tmpNodeL.right:
				queue.append(tmpNodeL.right)
		return True


if __name__ == '__main__':
    print(1)