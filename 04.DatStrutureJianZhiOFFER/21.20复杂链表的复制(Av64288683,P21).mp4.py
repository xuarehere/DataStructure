# -*- coding:utf-8 -*-
'''
21.20复杂链表的复制(Av64288683,P21).mp4
## 14.复杂链表的复制

**输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）**


难点
复制新的节点：
1、复制
2、随机指向

'''


'''
# 正确解法 1：
# 正确解法
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
      def Clone(self, pHead):
        # write code here

        #判断当pHead 为空值的时候 返回的是none

        if pHead == None:
            return None
        # 复制一个一样的node， 并且添加到之前的链表的每一个node后面
        pTmp = pHead
        while pTmp:
            #把第一个 A 的值 赋给 node 为A‘
            node = RandomListNode(pTmp.label)
            #此时 node A' 的结点指向的是 原来A 的结点指向的 值
            node.next = pTmp.next
            #将原来A 的结点指向的值 改为 A’
            pTmp.next = node
            #将 我们要操作的指针 向后移动 操作下一个 需要复制的元素，即为 A‘ 结点 指向的元素
            pTmp = node.next
        # 实现新建的node的random的指向
        pTmp = pHead
        while pTmp:
            #如果现在操作的这个指针的元素，存在一个 random 的结点
            if pTmp.random:
                #那么 这个A 的结点指向的（A’）的random结点指向的 值 为 A 的random的结点指向的值，指向的结点(也就是它的下一个值)上图更清楚明白。
                pTmp.next.random = pTmp.random.next
            #建好 这个元素的 random 的值，然后移动 指针 到下一个元素，来 建立 下一个 复制的元素的random 结点的指向。
            #当前元素 下一个的下一个 是复制的元素 是需要添加random 指向的元素。
            pTmp = pTmp.next.next
        # 断开原来的node 和 新的node 之间的链接
        #最后 为断开 链接 的操作
        pTmp = pHead
        #复制的新链表的表头A’ 为 旧链表 A 的结点指向的 下一个值A‘
        newHead = pHead.next
        #复制的新链表的第一个值A’ 为 旧链表 A 的结点指向的 下一个值A‘
        pNewTmp = pHead.next

        while pTmp:
            #print(pTmp.label)
            #将旧链表 A 的指向结点 改为  A‘ 的指向的下一个 的B。
            pTmp.next = pTmp.next.next
            #如果新的 链表 的元素有指向的下一个的指针
            if pNewTmp.next:
                #那么就把 这个元素的A’ 的结点指向 改为 A‘ 下一个 B 的下一个 的B’
                pNewTmp.next = pNewTmp.next.next
                #然后再 将 新链表的指针移 位，来断开下一个 链接，也就是 指针改为了 B‘
                pNewTmp = pNewTmp.next
            #上面新链表的元素指针改好了，再更改 下一个旧链表的 元素 也就是 上三行代码 之前改好的 A 的结点指向的B
            pTmp = pTmp.next
            #如此循环下去，改变所有的 新链表，旧链表的指向。
        #最后返回这个复制好的新链表。
        return newHead

'''




#  -------------------------------------------------------------------

'''
正确解法 2 

# 正确解法
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
      def Clone(self, pHead):
        # write code here
		# 第二种方法：
		import copy
		chead = copy.deepcopy(pHead)
		return chead
'''


'''
# 解法 3 ， 有个BUG
## 以下的方式是错误的，错在那儿？？
## 思路：
先复制正常的链表
然后在复制random 链表

# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead === None:
            return None
        
        newHead = RandomListNode(0)
        tmpNode = newHead
        
        tmp_pHead = pHead
        # copy normal
        while tmp_pHead:
            newNode = RandomListNode( tmp_pHead.label )
            # tmpNode.label = pHead.label
            tmpNode.next = newNode.next
            
            tmpNode = tmpNode.next
            tmp_pHead = tmp_pHead.next
        
        newHead = newHead.next
        tmpNode = newHead        
        tmp_pHead = pHead
        # copy random
        while tmp_pHead:
            if tmp_pHead:
                tmpNode.random = tmp_pHead.random
            tmp_pHead = tmp_pHead.next
            tmpNode = tmpNode.next
                
        return newHead


'''

'''
方法 3 正确解法
'''
# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
	# 返回 RandomListNode
	def Clone(self, pHead):
		# write code here
		if pHead == None:
			return None

		newHead = RandomListNode(0)
		tmpNode = newHead

		tmp_pHead = pHead
		# copy normal
		while tmp_pHead:
			newNode = RandomListNode(tmp_pHead.label)
			# tmpNode.label = pHead.label
			# tmpNode.next = newNode.next
			tmpNode.next = newNode

			tmpNode = tmpNode.next
			tmp_pHead = tmp_pHead.next

		newHead = newHead.next
		tmpNode = newHead
		tmp_pHead = pHead
		# copy random
		while tmp_pHead:
			if tmp_pHead.random:
				tmpNode.random = tmp_pHead.random
			tmp_pHead = tmp_pHead.next
			tmpNode = tmpNode.next

		return newHead

a = RandomListNode(1)
a.next= RandomListNode(2)
a.random = RandomListNode(22)
a.next.next= RandomListNode(4)
a.next.next.next= RandomListNode(5)
a.next.next.random= RandomListNode(55)
a.next.next.next.next= RandomListNode(9
									  )
b = Solution()
print( b.Clone(a))