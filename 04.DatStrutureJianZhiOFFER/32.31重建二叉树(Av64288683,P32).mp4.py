# -*- coding:utf-8 -*-
'''
32.31重建二叉树(Av64288683,P32).mp4


## 25.重建二叉树

**输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。**

扩展：
通过某两个序列（先序遍历、中序遍历、后序遍历中任意两个）重建二叉树

'''
'''
下面的代码有BUG

先序遍历：根左右
中序遍历：左根右

思路：先序遍历的第一个元素是根，把中序遍历的分为左右子树，同时把先序遍历的左右也划分了左右部分
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
	# 返回构造的TreeNode根节点
	def reConstructBinaryTree(self, pre, tin):
		# write code here
		if pre == None or tin == None:
			return None
		if len(pre) != len(tin):
			return None

		root = pre[0]
		print(root)
		rootIndex = tin.index(root)
		rootNode = TreeNode(root)

		tinLeft =  tin[0:rootIndex]
		tinRight = tin[rootIndex + 1:]

		preLeft =  pre[1:rootIndex + 1]
		preRight = pre[rootIndex + 1:]

		NodeLeft = self.reConstructBinaryTree(preLeft, tinLeft)
		NodeRight = self.reConstructBinaryTree(preRight, tinRight)

		rootNode.left = NodeLeft
		rootNode.right = NodeRight

		return rootNode


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
'''

#
# pre = [1,2,4,7,3,5,6,8]
# tin = [4,7,2,1,5,3,8,6]
#
# test = Solution()
# print( test.reConstructBinaryTree(pre,tin))
#
#




'''
正确代码
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
	# 返回构造的TreeNode根节点
	def reConstructBinaryTree(self, pre, tin):
		# write code here
		if pre == [] or tin == []:
			return None
		if len(pre) != len(tin):
			return None

		root = pre[0]
		print(root)
		rootIndex = tin.index(root)
		rootNode = TreeNode(root)

		tinLeft = tin[0:rootIndex]
		tinRight = tin[rootIndex + 1:]

		preLeft = pre[1:rootIndex + 1]
		preRight = pre[rootIndex + 1:]

		NodeLeft  = self.reConstructBinaryTree(preLeft, tinLeft)
		NodeRight = self.reConstructBinaryTree(preRight, tinRight)

		rootNode.left = NodeLeft
		rootNode.right = NodeRight

		return rootNode

