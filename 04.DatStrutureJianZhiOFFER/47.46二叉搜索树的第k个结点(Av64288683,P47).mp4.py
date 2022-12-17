# 47.46二叉搜索树的第k个结点(Av64288683,P47).mp4.py

'''
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，
按结点数值大小顺序第三小结点的值为4。

'''
# -*- coding:utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	# 返回对应节点TreeNode
	def KthNode(self, pRoot, k):
		# write code here
		if pRoot == None or k < 1:
			return None
		midList = []

		def midOrder(root):
			if root == None:
				return None
			midOrder(root.left)
			midList.append(root)
			midOrder(root.right)

		midOrder(pRoot)
		if len(midList) < k:
			return None
		return midList[k - 1]

if __name__ == '__main__':

	libao = [1, 3,8,15,25,40,60,90,130,190,260,450]
	print(len(libao) )
	index = 0
	for i in libao:
		if i == 40 :
			print("index ", index)
			break
		index +=1
	sum = 0
	for i in range(index+1, len(libao)):
		# print(i)
		sum +=libao[i]
	print("all libao:", sum)

	# dianquan
	libaoUnint = 50
	libaoUnintDianquan = 4600

	print("lack libao:%d;	libaoUnit:%d, libaoUnintDianquan=%d;		  "%(sum, libaoUnint, libaoUnint))
	print("[lack libao] / liBaoUnit = %f, dianQun = ([lack libao] / liBaoUnit) * liBaoUnitDianquan =  "%(sum/libaoUnint),
		  (sum/libaoUnint)*libaoUnintDianquan)



'''
下面的方式不行
问题出在哪儿

'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	# 返回对应节点TreeNode
	def KthNode(self, pRoot, k):
		# write code here
		if not pRoot:
			return None
		if k < 1:
			return None

		count = 0

		def midOrder(root, k):
			if not root:
				return 0
			left = midOrder(root.left, k)
			# root.val
			count += 1
			if count == k:
				return root.val
			elif count > k:
				return 0
			right = midOrder(root.right, k)

			return left + right

		return midOrder(root, k)


''''
下面的代码有问题

用例:
{8,6,10,5,7,9,11},1

对应输出应该为:

5

你的输出为:

list index out of range
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:
            return None
        if k <0:
            return None

        rootValue = []
        def midOrder(root):
            if not root:
                return None
            midOrder(root.left)
            rootValue.append(root.val)
            midOrder(root.right)

        midOrder(pRoot)
        if len(rootValue) > k:
            return None
        else:
            return rootValue[k]