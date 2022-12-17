# -*- coding:utf-8 -*-
'''
9.08两个栈实现一个队列(Av64288683,P9).mp4



## 1. 两个栈实现一个队列：[^本题考点 队列 栈]

**用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。**


'''

# -*- coding:utf-8 -*-
class Solution:
	def __init__(self):
		self.acceptStack = []
		self.outputStack = []

	def push(self, node):
		self.acceptStack.append(node)

	def pop(self):
		if self.outputStack == []:
			while self.acceptStack :
				self.outputStack.append( self.acceptStack.pop() )

		if self.outputStack :
			return self.outputStack.pop()
		else:
			return None