# -*- coding:utf-8 -*-

'''
20.19合并两个排序的链表(Av64288683,P20).mp4

## 16.合并两个排序的链表 [^本题考点  链表]

**输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。**


'''

### 方式一
### 下面的代码有 BUG
# -*- coding:utf-8 -*-
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
	# 返回合并后列表
	def Merge(self, pHead1, pHead2):
		# write code here

		if pHead1 == None and pHead2 == None:
			return None
		elif pHead1 == None:
			return pHead2
		elif pHead2 == None:
			return pHead1

		retNode = None
		retHead = None
		while pHead1 or pHead2:
			if pHead1 and pHead2:
				if pHead1.val <= pHead2.val:
					tmpNode = ListNode(pHead1.val)
					if retNode == None:
						retNode = tmpNode
						retHead = retNode
					else:
						retNode.next = tmpNode
						retNode = retNode.next
					pHead1 = pHead1.next

				else:
					tmpNode = ListNode(pHead2.val)
					if retNode == None:
						retNode = tmpNode
						retHead = retNode
					else:
						retNode.next = tmpNode
						retNode = retNode.next
					pHead2 = pHead2.next
			else:
				if pHead1:
					retNode.next = pHead1
				if pHead2:
					retNode.next = pHead2

		return retHead

'''


'''
### BUG 修复
# 思路：创建一个新的链表M，然后对两个输入的链表A,B进行比较，小的就放到M链表 M 中
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
	# 返回合并后列表
	def Merge(self, pHead1, pHead2):
		# write code here

		if pHead1 == None and pHead2 == None:
			return None
		elif pHead1 == None:
			return pHead2
		elif pHead2 == None:
			return pHead1

		retNode = None
		retHead = None
		while pHead1 or pHead2:
			if pHead1 and pHead2:
				if pHead1.val <= pHead2.val:
					tmpNode = ListNode(pHead1.val)
					if retNode == None:
						retNode = tmpNode
						retHead = retNode
					else:
						retNode.next = tmpNode
						retNode = retNode.next
					pHead1 = pHead1.next

				else:
					tmpNode = ListNode(pHead2.val)
					if retNode == None:
						retNode = tmpNode
						retHead = retNode
					else:
						retNode.next = tmpNode
						retNode = retNode.next
					pHead2 = pHead2.next
			else:
				if pHead1:
					retNode.next = pHead1
				if pHead2:
					retNode.next = pHead2
				break

		return retHead







a = ListNode(1)
a.next = ListNode(3)
a.next.next = ListNode(5)
a.next.next.next = ListNode(9)

b = ListNode(2)
b.next = ListNode(4)
b.next.next = ListNode(10)
b.next.next.next= ListNode(13)

print( Solution().Merge(a, b))



'''
## 方式二 有问题，没有解决

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        
        if pHead1 == None and  pHead2 ==None:
            return None
        elif pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        
        curHead1  = pHead1
        nextHead1 = pHead2.next
        curHead2  = pHead2
        nextHead2 = pHead2.next
        retNode = None
        if curHead1.val <= curHead2.val:
            retNode = curHead1
        else:
            retNode = curHead2
        while curHead1 and curHead2:
            if curHead1.val <= curHead2.val:
                curHead1.next = curHead2

                curHead1 = nextHead1
                nextHead1.next = nextHead1
            else:
                curHead2.nex = curHead1

                curHead2 = curHead2
                nextHead2.next = nextHead2
        return retNode



a = ListNode(1)
a.next = ListNode(3)
a.next.next = ListNode(5)
a.next.next.next = ListNode(9)

b = ListNode(2)
b.next = ListNode(4)
b.next.next = ListNode(10)
b.next.next.next= ListNode(13)

print( Solution().Merge(a, b))


