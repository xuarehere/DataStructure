# -*- coding:utf-8 -*-


'''
22.21两个链表的第一个公共结点(Av64288683,P22).mp4

## 15.两个链表之间的第一个公共结点

**输入两个链表，找出它们的第一个公共结点**
输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）

 这道题 有个疑问，返回值是什么？
 第一个链表，还是第二个链表？？
'''

'''
正确解法 
'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
	def FindFirstCommonNode(self, pHead1, pHead2):
		# write code here
		if pHead1 == None or pHead2 == None:
			return None

		tmpHead1 = pHead1
		tmpHead2 = pHead2

		while tmpHead1:
			tmpHead2 = pHead2
			while tmpHead2:
				if tmpHead1.val == tmpHead2.val:
					return tmpHead1
				tmpHead2 = tmpHead2.next
			tmpHead1 = tmpHead1.next
		return None