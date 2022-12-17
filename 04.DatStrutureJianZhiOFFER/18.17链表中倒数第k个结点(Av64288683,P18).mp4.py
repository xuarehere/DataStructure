# -*- coding:utf-8 -*-
'''
18.17链表中倒数第k个结点(Av64288683,P18).mp4

## 12.链表中的倒数第k个结点[^本题考点 *链表*]

**输入一个链表，输出该链表中倒数第k个结点。**


'''
'''
下面解法不通过？错误在哪儿

注意审题，返回的是节点
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def FindKthToTail(self, head, k):
		# write code here
		import copy
		if head == None:
			return None
		count = 0
		tmpHead = copy.deepcopy(head)
		while head:
			head = head.next
			count += 1

		tmpCount = 0
		while tmpHead:
			if tmpCount == (count - k):
				return tmpHead.val
			tmpHead = tmpHead.next
			tmpCount += 1
		return None

'''
答案错误:您提交的程序没有通过所有的测试用例点击对比用例标准输出与你的输出
case通过率为0.00%

用例:
1,{1,2,3,4,5}

对应输出应该为:

{5}

你的输出为:

{'int' object has no attribute 'val'

'''
a = ListNode(1 )
a.next = ListNode(2)
a.next.next  = ListNode(3)
a.next.next.next  = ListNode(4)
a.next.next.next.next  = ListNode(5)
a.next.next.next.next.next  = ListNode(6)
a.next.next.next.next.next.next  = ListNode(7)
b= Solution()
print( b.FindKthToTail(a, 3 ) )



## 正确解法1

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def FindKthToTail(self, head, k):
		# write code here
		# import copy

		if head == None:
			return None
		count = 0
		# tmpHead = copy.deepcopy(head)
		tmpHead = head
		while head :
			head = head.next
			count +=1

		tmpCount = 0
		while tmpHead:
			if tmpCount == (count-k):
				return tmpHead
			tmpHead = tmpHead.next
			tmpCount +=1
		return None




## 正确解法 2

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def FindKthToTail(self, head, k):
		# write code here

		if head == None or k < 0:
			return None

		firstPoint = head
		secondPoint = head
		for i in range(k):
			if firstPoint == None:
				return None
			firstPoint = firstPoint.next

		while firstPoint:
			firstPoint = firstPoint.next
			secondPoint = secondPoint.next

		return secondPoint