# -*- coding:utf-8 -*-
'''
# 37.36二叉树中和为某一值的路径(Av64288683,P37).mp4

## 30.二叉树中和为某一值的路径

**输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往
一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)**



# # 题目
# 题目描述
#
# > 输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直
到叶结点所经过的结点形成一条路径。(注意:
# > 在返回值的list中，数组长度大的数组靠前)



不会
不会
不会

思路：
解法一：
使用层次遍历法，对其进行扫描读取，每一次读到二叉树的底部的时候，进行检查，看是不是相等
然后，期间为每一个节点创建一个不同的路径储存

解法二：
深度优先遍历如何做？
我的方法是深度优先，做的不对，后面代买调试不出来

'''



# 实现
#
# ```python


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	# 返回二维列表，内部每个列表表示找到的路径
	def FindPath(self, root, expectNumber):
		import copy
		# write code here
		if root == None:
			return []
		queue1 = [root]
		ret = []
		viaList = [[root.val]]

		while queue1:
			tmpNode = queue1[0]
			tmpViaList = viaList[0]
			if tmpNode.left == None and tmpNode.right == None:
				if sum(tmpViaList) == expectNumber:
					# ret.append(tmpViaList)
					ret.insert(0, tmpViaList)
			if tmpNode.left:
				queue1.append(tmpNode.left)

				newTmpViaList = copy.copy(tmpViaList)
				newTmpViaList.append(tmpNode.left.val)
				viaList.append(newTmpViaList)
				# 方式一：错
				# viaList.append(tmpViaList.append(tmpNode.left.val))  # 错？

				# 方式二：错
				'''
				tmpViaList.append(tmpNode.left.val)
				viaList.append(tmpViaList)
				'''

				if tmpNode.right:
					queue1.append(tmpNode.right)

					newTmpViaList = copy.copy(tmpViaList)
					newTmpViaList.append(tmpNode.right.val)
					viaList.append(newTmpViaList)

				# viaList.append(tmpViaList.append(tmpNode.right.val))
				del queue1[0]
				del viaList[0]
			return ret

	# ```



## 通过代码
## 通过代码

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	# 返回二维列表，内部每个列表表示找到的路径
	def FindPath(self, root, expectNumber):
		# write code here
		import copy
		if not root:
			return []

		queue = [root]
		rootPath = [[root.val]]
		retPath = []
		while queue:
			tmpNode = queue.pop(0)
			tmpPath = rootPath.pop(0)
			if (tmpNode.left == None) and (tmpNode.right == None) and (sum(tmpPath) == expectNumber):
				# retPath.append(tmpPath)
				retPath.insert(0, tmpPath)

			if tmpNode.left:
				queue.append(tmpNode.left)

				newPath = copy.deepcopy(tmpPath)
				newPath.append(tmpNode.left.val)
				rootPath.append(newPath)

			if tmpNode.right:
				queue.append(tmpNode.right)

				newPath = copy.deepcopy(tmpPath)
				newPath.append(tmpNode.right.val)
				rootPath.append(newPath)
		return retPath



'''
不会
我的解法
我的解法
我的解法
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
	# 返回二维列表，内部每个列表表示找到的路径
	def FindPath(self, root, expectNumber):
		# write code here
		if root == None:
			return None
		rootTmp = []
		rootPath = []

		def preOrder(root):
			if root == None:
				return None

			rootTmp.append(root.val)

			if (sum(rootTmp) == expectNumber) and (root.left == None) and (root.right == None):
				if rootPath == []:
					rootPath.append(rootTmp)
				else:
					for i in range(len(rootPath)):
						if len(rootPath[i]) >= len(rootTmp):
							pass
						else:
							rootPath.insert(i, rootTmp)
							break
			preOrder(root.left)
			# rootTmp.pop(-1) if rootTmp != [] else pass
			# if rootTmp != []:
			# 	rootTmp.pop(-1)
			# 	pass
			preOrder(root.right)

		preOrder(root)
		return rootPath

'''

前序遍历序列	{1,2,4,7,3,5,6,8}
中序遍历序列	{4,7,2,1,5,3,8,6}，则重建二叉树并返回

         1
       /  \	
      2    3
     /\    /\
    4     5  6
   /\        /\
     7	    8
'''

root = TreeNode(1)

root7 =  TreeNode(7)

root4 =  TreeNode(4)
root4.right = root7

root2 =  TreeNode(2)
root2.left = root4

root.left = root2

# ==========
root8 =  TreeNode(8)

root6 =  TreeNode(6)
root6.left = root6

root3 =  TreeNode(3)
root3.right = root6
root3.left  = root3 =  TreeNode(5)
root.right = root3

a = Solution()
print( a.FindPath(root, 14))






'''
# 20200401 
### 没有通过的代码


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root :
            return []
        
        stack1 =[root]
        rootPath=[[root.val]]
        ret = []
        while stack1:
            tmpNode = stack1.pop(0)
            tmpPath = rootPath.pop(0)
            # tmpPath.append(tmpNode.val)
            if sum(tmpPath) == expectNumber:
                ret.insert(0, tmpPath)
            
            if tmpNode.left:
                stack1.append(  tmpNode.left )
                tmpPath.append(tmpNode.left.val )
                rootPath.append(tmpPath)
            
            if tmpNode.right:
                stack1.append(  tmpNode.right )
                tmpPath.append(tmpNode.right.val )
                rootPath.append(tmpPath)
        return ret 
                

'''
