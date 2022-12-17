# -*- coding:utf-8 -*-

'''
19.18反转链表(Av64288683,P19).mp4

## 13.反转链表[^本题考点 *链表*]

** 输入一个链表，反转链表后，输出新链表的表头。**

'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
	# 返回ListNode
	def ReverseList(self, pHead):
		# write code here
		if pHead == None:
			return None

		tmp = []
		while pHead:
			tmp.append(pHead.val)
			pHead = pHead.next

		newHead = ListNode(tmp.pop(-1))
		tmpNode = None
		tmpHead = newHead
		while tmp:
			tmpNode = ListNode(tmp.pop(-1))
			tmpHead.next = tmpNode
			tmpHead = tmpHead.next

		return newHead



'''
解法 2 
'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
	# 返回ListNode
	def ReverseList(self, pHead):
		# write code here

		if pHead == None:
			return None
		revNode = None
		while pHead:
			tmpNode = ListNode(pHead.val)
			pHead = pHead.next

			tmpNode.next = revNode
			revNode = tmpNode

		return revNode



