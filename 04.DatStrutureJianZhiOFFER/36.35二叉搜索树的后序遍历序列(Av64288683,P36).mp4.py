# -*- coding:utf-8 -*-
'''
36.35二叉搜索树的后序遍历序列(Av64288683,P36).mp4

## 29.二叉搜索树的后序遍历序列

**输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。**

'''

''''
做到这里，做不出来了

'''
# -*- coding:utf-8 -*-
class Solution:
	def VerifySquenceOfBST(self, sequence):
		# write code here
		if not sequence:
			return False

		root = sequence[-1]
		for i in range(len(sequence) - 2, -1):
			if sequence[i] < root and root < sequence[i + 1]:
				mid = i
				break
		left = self.VerifySquenceOfBST(sequence[:mid + 1])
		right = self.VerifySquenceOfBST(sequence[mid + 1:])

		return



''''
做到这里，做不出来了  == >  补充

'''


class Solution:
	def VerifySquenceOfBST(self, sequence):
		# write code here
		if not sequence:
			return False

		root = sequence.pop()
		l = len(sequence)
		mid = None

		for i in range(l):
			if sequence[i] > root and mid == None:
				mid = i
			if mid != None and sequence[i] < root:
				return False

		if sequence[:mid] == []:
			# if sequence[:mid ] == []:
			left = True
		else:
			left = self.VerifySquenceOfBST(sequence[:mid])

		if sequence[mid:] == []:
			right = True
		else:
			right = self.VerifySquenceOfBST(sequence[mid:])

		return left and right
'''
        15
     /     \
   10        20
  / \        / \
4    11    18    25
'''

alist = [4,11,10,18,25,20,15]
test = Solution()
print( test.VerifySquenceOfBST(alist) )