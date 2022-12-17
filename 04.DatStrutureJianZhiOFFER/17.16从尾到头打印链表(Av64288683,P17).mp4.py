# -*- coding:utf-8 -*-
'''
17.16从尾到头打印链表(Av64288683,P17).mp4


## 11. 从栈尾到栈头打印链表 [^本题知识点 *链表*]

**输入一个链表，按链表值从尾到头的顺序返回一个`ArrayList`。**


'''





# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        import copy
        if listNode == None :
            return []
        alist = []
        while listNode !=None:
            alist.append(listNode.val)
            listNode = listNode.next
        tmp = []
        while alist:
            tmp.append(alist.pop(-1))
        return tmp




''''
方式二

'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# 返回从尾部到头部的列表值序列，例如[1,2,3]
	def printListFromTailToHead(self, listNode):
		# write code here
		if listNode == None:
			return []
		alist = []
		while listNode != None:
			# alist.append(listNode.val)
			alist.insert(0, listNode.val)
			listNode = listNode.next
		return alist
