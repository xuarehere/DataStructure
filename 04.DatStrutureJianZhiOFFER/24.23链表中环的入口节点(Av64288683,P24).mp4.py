# -*- coding:utf-8 -*-
'''
24.23链表中环的入口节点(Av64288683,P24).mp4


## 18.链表中环的入口点 [^本题知识点  链表]

**给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。**
'''

'''
有bug 的代码

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None:
            return None
        
        curHead = pHead
        fastHead = pHead.next
        while curHead:
            if fastHead == curHead:
                return curHead
#             if fastHead and  fastHead.next and fastHead.next.next:
            if fastHead and  fastHead.next:
                fastHead = fastHead.next.next
            else:
                return None
            curHead = curHead.next
        return None
'''